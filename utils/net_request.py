import requests
from requests.adapters import HTTPAdapter


class NetRequest:
    """网络请求统一封包"""

    def __init__(self):
        self.session = requests.Session()
        self.session.mount("http://", HTTPAdapter(max_retries=3))
        self.session.mount("https://", HTTPAdapter(max_retries=3))
        self.timeout = 300

    def post(self, url, **kwargs):
        return self.session.post(url=url, timeout=self.timeout, **kwargs)

    def get(self, url, **kwargs):
        return self.session.get(url=url, timeout=self.timeout, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(url=url, timeout=self.timeout, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, timeout=self.timeout, **kwargs)
