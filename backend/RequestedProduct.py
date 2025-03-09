from backend.Product import *
import datetime

class RequestedProduct:
    def __init__(self, product, seller):
        self.__product = product
        self.__seller = seller
        self.__create_at = datetime.now()

        #status Approvee Idle Reject
        self.__status = "Idle"

    @property
    def product(self):
        return self.__product
    
    @property
    def seller(self):
        return self.__seller
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def status(self):
        return self.__is_reject

    def update_status(self, new_status):
        self.__status = new_status
        return "success"


