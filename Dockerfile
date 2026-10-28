
FROM python:3.12-slim

RUN useradd --create-home appuser

USER appuser

WORKDIR /home/appuser

COPY app.py server.py ./

EXPOSE 8000

CMD ["python", "server.py"]
