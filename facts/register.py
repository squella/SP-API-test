from interactions.reqres import ReqresClient

class RegisterUserFacts(object):
    _reqres = ReqresClient()
    _resource = "register"
    
    @classmethod
    def register(cls, register):
        data = register.to_dict()
        
        status, header, body = cls._reqres.post(cls._resource, data)
        
        return status, header, body

        
        
        
        
        