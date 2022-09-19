from interactions.reqres import ReqresClient


class SingleUserFacts(object):
    _reqres = ReqresClient()
    _resource = "users"
    
    @classmethod
    def get_single_user(cls, param):
        status, header, body = cls._reqres.get(cls._resource, param)
        return status, header, body
        