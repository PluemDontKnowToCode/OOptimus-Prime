from backend.Object import *
from backend.Comment import *

class Product(Object):

    #image is list na
    def __init__(self, name = '', id = '', price = 0, description = '', img1 = '', category = '', stock = 0,comment_list = [],market = None):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__img = img1
        self.__category = category
        self.__comment_list = comment_list
        self.__stock = stock
        self.__market = market
        super().__init__(id)

    
    @property
    def make_detail(self): return [self.__name, self.__price, self.__stock, self.__description]

    @property
    def get_comment_dict(self):
        res = []
        for i in self.__comment_list:
            res.append(i.to_json())
        return res

    @property
    def detail(self): return [self.make_detail, self.get_comment_dict]
    
    @property
    def name(self): 
        return self.__name

    @property
    def price(self):
        return self.__price
    
    @property
    def description(self):
        return self.__description
    
    @property
    def image(self):
        return self.__img
    
    @property
    def category(self):
        return self.__category
    
    @property
    def stock(self): 
        return self.__stock
    
    def to_json(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "price" : self.price,
            "description" : self.description,
            "img" : self.image,
            "category" : self.category,
            "stock": self.__stock,
            "comment" : [i.to_json() for i in self.__comment_list]
        }
        
    def add_comment(self, comment : Comment):
        res = "Fail"
        if isinstance(comment, Comment):
            self.__comment_list.append(comment)
            res = "Done"
        return res
    
    def update_stock(self, a):
        self.__stock += a
        
    def is_greater_than_me(self, amount): return amount > self.__stock