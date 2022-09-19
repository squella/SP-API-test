from interactions.reqres import ReqresClient

class ListUserFacts(object):
    _reqres = ReqresClient()
    _resource = "users"
    
    @classmethod
    def get_list_user(cls, qs_param):
        status, header, body = cls._reqres.get_query_string(
            cls._resource, qs_param)
        return status, header, body     
        