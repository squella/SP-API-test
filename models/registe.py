
class RegisteUnsuccessfulRequest(object):
    def __init__(self, email: str = "") -> None:
        self.email = email
        

    def to_dict(self) -> dict:
        return self.__dict__
