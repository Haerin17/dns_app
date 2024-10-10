FROM python:3.8-slim

WORKDIR /app

COPY auth_server.py .

RUN pip install flask

CMD ["python", "auth_server.py"]
