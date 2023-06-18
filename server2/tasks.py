from celery import Celery
import time
from kombu import Queue
from os import getenv


backend = getenv("BACKEND", "rpc://")
broker = getenv("BROKER", "rpc://")

celery_app = Celery(main="tasks", backend=backend, broker=broker)
celery_app.conf.task_queues = (
    Queue("wait_worker-queue", routing_key="wait_worker-queue"),
)
celery_app.conf.task_routes = {
    "tasks.wait_worker": {
        "queue": "wait_worker-queue",
        "routing_key": "wait_worker-queue",
    },
}
celery_app.autodiscover_tasks()


@celery_app.task(
    bind=True,
    max_retries=3,
    queue="wait_worker-queue",
)
def wait_worker(self, wait_time):
    time.sleep(wait_time)
    return "Waited"
