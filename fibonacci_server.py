from flask import Flask, request, jsonify
import socket
import json

app = Flask(__name__)

# 注册服务
@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = int(data['as_port'])

    # 发送注册请求到权威服务器
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    registration_msg = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10"
    sock.sendto(registration_msg.encode(), (as_ip, as_port))
    return jsonify({"status": "Registered"}), 201

# 计算斐波那契数
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    try:
        n = int(number)
        result = fib(n)
        return jsonify({"fibonacci": result}), 200
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
