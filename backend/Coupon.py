#region Coupon
from datetime import datetime
from backend.Cart import *

class Coupon(Object):
    def __init__(self, id, discount_percent,less_amount : float,product_count: int = 0, start_time: datetime = None , end_time: datetime = None):
        super().__init__(id)
        self.__discount_percent = discount_percent
        self.__less_amount = less_amount
        self.__product_count = product_count
        self.__start_time = start_time
        self.__end_time = end_time

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
    def start_time(self):
        return self.__start_time.strftime("%Y-%m-%d")
    
    @property
    def end_time(self):
        return self.__end_time.strftime("%Y-%m-%d")
    
    def to_json(self):
        return {
            "id" : super().id,
            "discount_percent" : self.__discount_percent,
            "less_amount" : self.__less_amount,
            "product_count" : self.__product_count,
            "start_time" : self.__start_time.strftime("%Y-%m-%d"),
            "end_time" : self.__end_time.strftime("%Y-%m-%d")
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