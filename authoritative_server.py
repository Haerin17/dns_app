import socket

# 存储 DNS 记录的字典
dns_records = {}

# 启动 UDP 服务器，监听注册和查询请求
def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 53533))

    print("Authoritative Server is running on port 53533...")

    while True:
        print("Waiting for incoming connections...")
        data, addr = sock.recvfrom(1024)
        print(f"Received data from {addr}")
        
        message = data.decode().split('\n')
        if message[0] == "TYPE=A":
            if len(message) == 4:  # 注册请求
                name = message[1].split('=')[1]
                value = message[2].split('=')[1]
                dns_records[name] = value
                print(f"Registered: {name} -> {value}")
                sock.sendto("Registered".encode(), addr)
            elif len(message) == 2:  # 查询请求
                name = message[1].split('=')[1]
                if name in dns_records:
                    response = f"TYPE=A\nNAME={name}\nVALUE={dns_records[name]}\nTTL=10"
                    sock.sendto(response.encode(), addr)
                else:
                    sock.sendto("Not found".encode(), addr)

if __name__ == '__main__':
    start_server()
