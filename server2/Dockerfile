FROM python:3.11.2-slim-buster

# ENV GUNICORN_CMD_ARGS="-k uvicorn.workers.UvicornWorker --bind=0.0.0.0:5000 --workers=8 --timeout=90"
WORKDIR /etc/example_app_1

# Software updates beware with caching you might be behind a few versions from current package updates just because of the way Docker works
RUN apt-get update && \
    apt-get -y install ca-certificates \ 
    openssl \
    python3-dev \
    build-essential \ 
    libssl-dev \ 
    libffi-dev \ 
    libsasl2-dev

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /etc/example_app_1

EXPOSE 5000
# ENTRYPOINT ["gunicorn", "wsgi:app"]