from configuration import Configuration
import json


class SingletUsers(object):
    def __init__(self, data: dict = {}, support: dict = {}) -> None:
        self.data = data
        self.support = support


    @classmethod
    def from_file(cls, filename: str):
        path = f"{Configuration().test_data_path}/single-user/{filename}.json"
        with open(path) as json_file:
            body = json.load(json_file)
            json_file.close()

        single_user = cls()
        single_user.data = body["data"]
        single_user.support = body["support"]

        return single_user
