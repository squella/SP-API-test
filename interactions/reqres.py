import requests
from configuration import Configuration

class ReqresClient(object):
    
    def __init__(self) -> None:
        self._api_url = Configuration().reqres_api_url
        self._version = Configuration().reqres_api_version
        self._allow_redirect = False
        self._content_type = "application/json"


    def get(self, resource, id):
        url = f"{self._api_url}/{self._version}/{resource}/{id}"
        response = requests.get(url,
                                allow_redirects=self._allow_redirect)

        status_code = response.status_code
        headers = response.headers
        body = response.json()

        return status_code, headers, body