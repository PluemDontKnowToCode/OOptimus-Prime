from backend.Account import *
from backend.Product import *

class Seller(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 0 ,address = [],image = "",selling_product = [], market = None):
        super().__init__(id, name,username, password, money,address, image, market)
        self.__selling_product = selling_product
    

    @property
    def selling_product(self):
        return self.__selling_product


    def add_product(self, product : Product):
        self.__selling_product.append(product)
        return "Seller Add Complete"

    def delete_product(self, product : Product):
        self.__selling_product.remove(product)
        return "Seller Remove Complete"

    def delete_product(self, product_id : str):
        product = super().market.get_product(product_id)
        self.__selling_product.remove(product)

