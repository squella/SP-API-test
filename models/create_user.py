
class CreateUserRequest(object):
    def __init__(self, name: str = "", job: str = "") -> None:
        self.name = name
        self.job = job

    def to_dict(self) -> dict:
        return self.__dict__
