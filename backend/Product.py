from backend.Object import *
from backend.Comment import *

class Product(Object):

    #image is list na
    def __init__(self, name = '', id = '', price = 0, description = '', img1 = '', category = '', stock = 0,market = None):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__img = img1
        self.__category = category
        self.__comment_list = []
        self.__stock = stock
        self.__market = market
        super().__init__(id)
    
    def __init__(self, d: dict,market):
        self.__name = d['name']
        self.__price = d['price']
        self.__description = d['description']
        self.__img = d['img']
        self.__category = d['category']
        self.__stock = d['stock']
        self.__market = market
        clist = []
        
        # print(market1.account_list) 
        for i in d['comment']:
            acc = self.__market.get_account(i['owner_id'])
            # print(f"{acc} {i['owner_id']}")
            c = Comment(acc.name, i['text'], i['star'], i['owner_id'])
            clist.append(c)
        self.__comment_list = clist
        super().__init__(d['id'])
    
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
    
    @stock.setter
    def stock(self, a):
        self.__stock = a
    
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