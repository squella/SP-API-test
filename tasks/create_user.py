from interactions.reqres import ReqresClient

class CreateUserTask(object):
    _reqres = ReqresClient()
    _resource = "users"
    
    @classmethod
    def create_user(cls, create_user):
        data = create_user.to_dict()
        
        status, header, body = cls._reqres.post(cls._resource, data)
        
        return status, header, body

        
        
        
        
        