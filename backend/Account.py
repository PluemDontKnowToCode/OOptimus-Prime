from backend.Object import *
from backend.Address import *

class Account(Object):
    def __init__(self, id = "", name = "", username = "", password ="", money = 0 ,image = "",market = None):
        super().__init__(id)
         #name use for login
        self.__name = name
        self.__password = password
        self.__username = username
        self.__image = image
        self.__money = money
        self.__market = market
        self.__address_list = []

    def __init__(self,d: dict, market = None):
        self.__name = d['name']
        self.__password = d['password']
        self.__username = d['username']
        self.__image = d['image']
        self.__money = d['money']
        self.__market = market
        temp = []
        for i in d['address']:
            temp.append(Address(i['district'], i['province'], i['zip_code'], i['phone']))
        self.__address_list = temp
        super().__init__(d['id'])
    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return self.__password
    
    @property 
    def username(self):
        return self.__username
    
    @property
    def image(self):
        return self.__image
    
    @property
    def money(self):
        return self.__money
    
    @property
    def market(self):
        return self.__market
    
    @property
    def address_list(self):
        return self.__address_list
    @property
    def cart(self):
        return None
    @property
    def coupon_list(self):
        return self.__coupon_list
    
    def update_money(self, amount):
        self.__money += amount

    def get_coupon(self):
        return None
    
    def self_verify(self, name, password):
        if name == self.__username and password == self.__password: return True
        return False
    
    def get_address(self):
        res = []
        for i in self.__address_list:
            res.append(i.to_json())
        return res