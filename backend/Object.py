class Object:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        # print("Sending my id")
        return self.__id

    def set_id(self, id1): self.__id = id1
    
    def Equal(self, id):
        return self.__id == id