FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD ./container_app/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A container_app.sellerie worker --concurrency=20 --loglevel=error