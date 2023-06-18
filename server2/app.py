#!/usr/bin/env python3
# coding: utf-8

import logging
import sys
import time

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from prometheus_fastapi_instrumentator import Instrumentator
from tasks import wait_worker

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.setLevel("INFO")

app = FastAPI(
    docs_url="/example1/docs",
    redoc_url="/example1/redoc",
)
Instrumentator().instrument(app).expose(app)

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,  # THIS IS FOR DEV PURPOSE, SHOULD BE INFO IN PROD
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)


@app.get("/healthz", status_code=200)
async def healthz():
    """Path used to check if the app is still up"""
    return {"health": "OK", "application": "example1"}


@app.post("/example1/wait/{wait}")
async def wait(wait: int):
    time.sleep(wait)
    return "Awaited"


@app.post("/example1/wait_celery/{wait}")
async def w_worker(wait: int):
    wait_worker.s().delay(wait_time=wait)
    return "Awaited"
