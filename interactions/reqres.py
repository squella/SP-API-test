import requests
from configuration import Configuration

class ReqresClient(object):
    
    def __init__(self) -> None:
        self._api_url = Configuration().reqres_api_url
        self._version = Configuration().reqres_api_version
        self._allow_redirect = False
        self._content_type = "application/json"


    def get_query_string(self, resource, qs):
        url = f"{self._api_url}/{self._version}/{resource}?{qs}"
        response = requests.get(url,
                                allow_redirects=self._allow_redirect)

        status_code = response.status_code
        headers = response.headers
        body = response.json()

        return status_code, headers, body

    def get(self, resource, param):
        url = f"{self._api_url}/{self._version}/{resource}/{param}"
        response = requests.get(url,
                                allow_redirects=self._allow_redirect)

        status_code = response.status_code
        headers = response.headers
        body = response.json()

        return status_code, headers, body
    
    def post(self, resource, payload):

        url = f"{self._api_url}/{self._version}/{resource}"
        response = requests.post(url, json=payload, 
                                 headers={"content-type": self._content_type},
                                 allow_redirects=self._allow_redirect)

        status_code = response.status_code
        headers = response.headers
        body = response.json()

        return status_code, headers, body