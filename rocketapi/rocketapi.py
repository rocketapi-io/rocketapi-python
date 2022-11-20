import requests


class RocketAPI:
    def __init__(self, token, threads=1):
        self.base_url = "https://v1.rocketapi.io/"
        self.token = token
        self.threads = threads
        self.max_timeout = 30

    def request(self, method, data):
        data['_threads'] = self.threads
        return requests.post(url=self.base_url + method, json=data, headers={'Authorization': f'Token {self.token}'}, timeout=self.max_timeout).json()
