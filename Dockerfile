FROM python:3.12-slim
WORKDIR /app
COPY app.py server.py ./
EXPOSE 8000
CMD ["python","server.py"]
