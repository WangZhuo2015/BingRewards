import os
from abc import abstractmethod

import requests


class Notification:
    @abstractmethod
    def notify(self, message):
        pass


class BarkNotification(Notification):
    def __init__(self, api_key=os.environ.get("BARK_API_KEY")):
        if api_key is None:
            raise Exception("Bark API Key is not set")
        self.api_key = api_key

    def notify(self, body, title="Bing Rewards"):
        # https://api.day.app/{api_key}}/Title/text
        # send http get request to the url
        requests.get(f"https://api.day.app/{self.api_key}/{title}/{body}")
