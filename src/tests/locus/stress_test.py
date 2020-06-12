import random
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0, 2)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def get_json(self):
        self.client.get("/api/v1/hello")
