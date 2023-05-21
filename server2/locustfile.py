from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def wait_async(self):
        self.client.post("/example1/wait_celery/4")
