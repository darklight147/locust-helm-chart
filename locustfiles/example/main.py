# -*- coding: utf-8 -*-

from locust import HttpUser, task, between
from lib.example_functions import choose_random_page
from random import choice


default_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_catalogs(self):
        self.client.get("/api/catalog", headers=default_headers)

    @task
    def get_catalog_id(self):
        choices = [1,2,3]

        random_choice = choice(choices)

        self.client.get("/api/catalog/{}".format(random_choice), headers=default_headers)

    @task
    def get_orders(self):
        self.client.get("/api/order", headers=default_headers)

    @task
    def get_order_id(self):
        choices = [1,2,3]

        random_choice = choice(choices)

        self.client.get("/api/order/{}".format(random_choice), headers=default_headers)

    @task
    def get_customers(self):
        self.client.get("/api/customer", headers=default_headers)

    @task
    def get_customer_id(self):
        choices = [1,2,3]

        random_choice = choice(choices)

        self.client.get("/api/customer/{}".format(random_choice), headers=default_headers)

