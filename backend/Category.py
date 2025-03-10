from backend.Product import *


#region Categories
class Category:

    #collect product as id
    def __init__(self,name):
        self.__name = name
        self.__product_list = []

    @property
    def name(self):
        return self.__name
    
    @property
    def product_list(self):
        return self.__product_list

    def get_product_list(self):
        res = []
        for i in self.__product_list:
            res.append(i.to_json())
        return res


    def add_product(self, product : Product):
        if isinstance(product, list):
            self.__product_list.extend(product)
        else:
            self.__product_list.append(product)
        return "success"
    def remove_product(self, product : Product):
        self.__product_list.remove(product)
        return "success"
#endregion