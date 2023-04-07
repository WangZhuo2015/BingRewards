import os
from abc import abstractmethod

import requests
from dotenv import load_dotenv


class Notification:
    @abstractmethod
    def notify(self, message):
        pass


class BarkNotification(Notification):
    def __init__(self, api_key=os.environ.get("BARK_API_KEY", None),
                 bark_server="https://api.day.app"):
        # if api_key is None:
        #     raise Exception("Bark API Key is not set")
        self.api_key = api_key
        self.bark_server = bark_server

    def notify(self, body, title="Bing Rewards"):
        # https://api.day.app/{api_key}}/Title/text
        # send http get request to the url
        print(f"{self.bark_server}/{self.api_key}/{title}/{body}")
        requests.get(f"{self.bark_server}/{self.api_key}/{title}/{body}")
