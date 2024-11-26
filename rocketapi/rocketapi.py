import requests


class RocketAPI:
    def __init__(self, token, max_timeout=30):
        """
        RocketAPI client.

        If your base_url is different from the default, you can reassign it after initialization.

        For more information, see documentation: https://docs.rocketapi.io/api/
        """
        self.base_url = "https://v1.rocketapi.io/"
        self.version = "1.0.9"
        self.token = token
        self.max_timeout = max_timeout

    def request(self, method, data):
        return requests.post(
            url=self.base_url + method,
            json=data,
            headers={
                "Authorization": f"Token {self.token}",
                "User-Agent": f"RocketAPI Python SDK/{self.version}",
            },
            timeout=self.max_timeout,
        ).json()
