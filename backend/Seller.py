from backend.Account import *
from backend.Product import *

class Seller(Account):
    def __init__(self, id):
        super().__init__(id)
        self.__selling_product = []

    @property
    def selling_product(self):
        return self.__selling_product

    def __init__(self, d: dict, market = None):
        super().__init__(d, market)

    def create_product(self, product : Product):
        self.__selling_product.append(product)

    def delete_product(self, product : Product):
        self.__selling_product.remove(product)

    def delete_product(self, product_id : str):
        product = super().market.get_product(product_id)
        self.__selling_product.remove(product)

