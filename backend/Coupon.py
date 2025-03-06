#region Coupon
from datetime import *
from backend.Cart import *

class Coupon(Object):
    def __init__(self, id, discount_percent,less_amount : float,product_count = 0, start_time = datetime.now(), end_time = 0):
        super().__init__(id)
        self.__discount_percent = discount_percent
        self.__less_amount = less_amount
        self.__product_count = product_count
        self.__start_time = datetime.strptime(start_time, "%Y-%m-%d")
        self.__end_time = datetime.strptime(end_time, "%Y-%m-%d")

    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    @property
    def discount_percent(self):
        return self.__discount_percent
    
    @property
    def less_amount(self):
        return self.__less_amount
    
    @property
    def product_count(self):
        return self.__product_count
    
    @property
    def product_accord(self):
        return self.__product_accord
    
    def to_json(self):
        return {
            "id" : super().id,
            "discount_percent" : self.__discount_percent,
            "less_amount" : self.__less_amount,
            "product_count" : self.__product_count,
            "start_time" : self.__start_time,
            "end_time" : self.__end_time
        }
    def check_condition(self, cart : Cart):
        if cart.size < self.__product_count: 
            return False
        if cart.calculate_price() < self.__less_amount:
            return False
        if datetime.now() < self.__start_time or datetime.now() > self.__end_time: 
            return False
        return True
#endregion