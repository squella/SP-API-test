
class ListUserTask(object):
    
    @classmethod
    def extract_object_by_id(cls, id: int, list_users: list) -> dict:
        obj = next((x for x in list_users if x["id"] == id), None)
        if obj == None:
            return print("Erro: Invalid input parameters")
        else:
            return obj