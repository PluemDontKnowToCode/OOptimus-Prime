class Object:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        # print("Sending my id")
        return self.__id

    def equal(self, id):
        return self.__id == id