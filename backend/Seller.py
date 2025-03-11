from backend.Account import *
from backend.Product import *
from backend.RequestedProduct import *

class Seller(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 10000 ,address = [],image = "user_imgpng.png",selling_product = [], market = None):
        super().__init__(id, name,username, password, money,address, image, market)
        self.__selling_product = selling_product
    

    @property
    def selling_product(self):
        return self.__selling_product
    def get_requested_product(self):
        all_request = self.market.requested_list
        res = []
        for i in all_request:
            if i.seller == self and i.status == "Idle":
                res.append(i.product)
        return res
    def create_product(self, name,price ,description, image_url, category, quantity):
        product = Product(name, self.market.generate_id(0), price ,description, img1=image_url, category=category, stock = quantity)
        r = RequestedProduct(product, self)
        self.market.add_requested(r)
        return "success"
    
    def add_product(self, product : Product):
        self.__selling_product.append(product)
        return "Seller Add Complete"


