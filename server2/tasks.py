from celery import Celery
import time


backend = "rpc://"
broker = f"pyamqp://default:default@localhost:{port}//"

celery_app = Celery(main="tasks", backend=backend, broker=broker)
celery_app.autodiscover_tasks()


@celery_app.task(bind=True, max_retries=3)
def wait_worker(self, wait_time):
    time.sleep(wait_time)
    return "Waited"
