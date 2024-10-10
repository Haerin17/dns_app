FROM python:3.8-slim

WORKDIR /app

COPY user_server.py .

RUN pip install flask

CMD ["python", "user_server.py"]
