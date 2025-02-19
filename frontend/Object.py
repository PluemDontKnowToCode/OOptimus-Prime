import enum

class Object:
    def __init__(self, id):
        self.__id = id

    def Equal(self, id):
        return self.__id == id

class Product(Object):
    def __init__(self, name, id, price, description, img1, catagory):
        super().__init__(id)
        self.__name = name
        self.__price = price
        self.__description = description
        self.__commnet_list = []
        self.__img = img1
        self.__catagory = catagory
    
    @property
    def make_detail(self): return [self.__name, self.__id, self.__price, self.__description]

    @property
    def get_comment_dict(self):
        res = []
        for i in self.__commnet_list:
            res.append(i.convert_to_dict)
        return res

    @property
    def detail(self): return [self.make_detail, self.get_comment_dict]
    
    @property
    def name(self): return self.__name

    @property
    def price(self):
        return self.__price
#region Account
class Account(Object):
    def __init__(self, id,name,username ,password, money,image,market):
        super().__init__(id)
         #use for login
        self.__name = name
        self.__password = password

        self.__username = username
        self.__image = image
        self.__money = money
        self.__market = market

    

class Customer(Account):
    def __init__(self, id, money = 0, market = None):
        super.__init__(id,money)
        self.__cart = Cart()
        self.__transaction = []
        
    def add_transaction(self,product_id,datetime):
        self.__transaction.append(Transaction(id,product_id,datetime))
        return
    
    def update_money(self, amount):
        self.__money += amount
        return
        
    def view_product_detail(self, product_id): return self.__market.view_product_detail(product_id)

    @property
    def cart(self):
        return self.__cart
    
    
    def cart_product(self):
        return self.__cart.product_list

class Seller(Account):
    def __init__(self, id):
        super().__init__(id)

class Admin(Account):
    def __init__():
        super().__init__(id)
#endregion
#region Transaction
class Transaction():
    def __init__(self, customer_id, product_id,datetime):
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__date = datetime

    def __str__(self):
        return f
#endregion
        
    
    


class Cart:
    def __init__(self):
        self.__product_List = []

    def remove_product(self, product_id):
        for i in self.__product_List:
            if i.Equal(product_id):
                self.__product_List.remove(i)
                return "Remove Complete"
        return  "Product Id Not found"

    @property
    def product_list(self):
        return self.__product_List
    

         


class Comment:
    def __init__(self, name, text, star : int):
        self.__name = name
        self.__text = text
        self.__star = star
    
    @property
    def convert_to_dict(self):
        return {
            "name": self.__name, 
            "text": self.__text,
            "star": self.__star
        }
    
    @property
    def name(self):
        return self.__name
    
    @property
    def text(self):
        return self.__text
    
    @property
    def star(self):
        return self.__star
    
class Market():
    def __init__(self):
        self.__account_list = []
        self.__product_list = []
        self.__coupon_list = []
        
    @property
    def account_list(self):
        return self.__account_list
    
    @property
    def product_list(self):
        return self.__product_list
    
    @property
    def coupon_list(self):
        return self.__coupon_list
    
    def add_account(self, account : Account):
        self.__account_list.append(account)
        
    def add_product(self, product : Product):
        self.__product_list.append(product)

    def purchase(self, user_id, address, coupon, money):
        return
    
    def get_account(self, user_id): 
        for i in self.__user_list:
            if i.Equal(user_id):
                return i
        return None
    
    def get_product(self, product_id):
        for i in self.__product_list:
            if i.Equal(product_id): 
                return i
        return None
    def get_coupon(self, coupon_id):
        for i in self.__product_list:
            if i.Equal(coupon_id): 
                return i
        return None
    def get_product_detail(self, product): 
        return product.detail
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        return self.get_product_detail(product)