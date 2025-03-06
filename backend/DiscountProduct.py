from backend.Product import *

class DiscountProduct(Product):
    def __init__(self, name, id, price, description, img1, category, discount_percent, expire_date):
        super().__init__(name, id, price, description, img1, category)
        self.__discount_percent = discount_percent
        self.__expire_date = expire_date

    @property
    def price(self):
        return super().__price * (100 - self.__discount_percent)
    
    @property
    def expire_date(self):
        return self.__expire_date