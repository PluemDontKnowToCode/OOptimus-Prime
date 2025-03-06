from backend.Product import *


#region Categories
class Categories:

    #collect product as id
    def __init__(self,name):
        self.__name = name
        self.__product = []

    @property
    def name(self):
        return self.__name
    
    @property
    def products(self):
        return self.__product
    
    def add_product(self, product : Product):
        if isinstance(product, list):
            self.__product.extend(product)
        else:
            self.__product.append(product)
        return "success"
    def remove_product(self, product : Product):
        self.__product.remove(product)
        return "success"
#endregion