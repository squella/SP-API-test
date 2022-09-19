from configuration import Configuration
import json

class ListUsers(object):
    def __init__(self, page: int = 0, per_page: int = 0, 
                 total: int = 0, total_pages: int = 0,
                 data: list = [], support: dict = {}) -> None:
        self.page = page
        self.per_page = per_page
        self.total = total
        self.total_pages = total_pages
        self.data = data
        self.support = support

    @classmethod
    def from_file(cls, filename: str):
        path = f"{Configuration().test_data_path}/list-users/{filename}.json"
        with open(path) as json_file:
            body = json.load(json_file)
            json_file.close()

        list_users = cls()
        list_users.page = body["page"]
        list_users.per_page = body["per_page"]
        list_users.total = body["total"]
        list_users.total_pages = body["total_pages"]
        list_users.data = body["data"]
        list_users.support = body["support"]

        return list_users