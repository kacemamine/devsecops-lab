
FROM python:3.12-slim

RUN useradd --create-home appuser

WORKDIR /home/appuser

COPY --chown=appuser:appuser app.py server.py ./

USER appuser

EXPOSE 8000

LABEL org.opencontainers.image.source="https://github.com/kacemamine/devsecops-lab"

CMD ["python", "server.py"]
