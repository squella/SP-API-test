
class StatusQuestions(object):
    @classmethod
    def is_ok(cls, status) -> bool:
        return status == 200

    @classmethod
    def is_created(cls, status) -> bool:
        return status == 201
    
    @classmethod
    def has_syntactic_error(cls, status) -> bool:
        return status == 400
