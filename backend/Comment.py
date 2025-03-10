#region Comment
class Comment:
    def __init__(self, name, text, star : int, new_id):
        self.__name = name
        self.__text = text
        self.__star = star
        self.__user_id = new_id
    
    def to_json(self):
        return {
            "name": self.__name, 
            "text": self.__text,
            "star": self.__star
        }
    
    @property
    def name(self):
        return self.__name
    
    @property
    def text(self):
        return self.__text
    
    @property
    def star(self):
        return self.__star
    
    @property
    def user_id(self):
        return self.__user_id
#endregion