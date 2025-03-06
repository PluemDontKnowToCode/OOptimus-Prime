from datetime import *

#region Transaction
class Transaction():
    def __init__(self, product_id):
        self.__product_id = product_id
        self.__date = datetime.now()

    def to_json(self):
        return {
            "customer_id" : self.__customer_id,
            "product_id" : self.__product_id,
            "date" : self.__date
        }
    
    
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def date(self):
        return self.__date
#endregion