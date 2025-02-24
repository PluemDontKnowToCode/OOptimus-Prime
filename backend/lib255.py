import enum
import datetime

class Object:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    def Equal(self, id):
        return self.__id == id

#region Comment
class Comment:
    def __init__(self, name, text, star : int):
        self.__name = name
        self.__text = text
        self.__star = star
        self.__sym = "✯"
    
    @property
    def convert_to_dict(self):
        return {
            "name": self.__name, 
            "text": self.__text,
            "star": self.__star * self.__sym
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
#endregion
#region Product
class Product(Object):

    #image is list na
    def __init__(self, name, id, price, description, img1, category):
        super().__init__(id)
        self.__name = name
        self.__price = price
        self.__description = description
        self.__img = img1
        self.__category = category
        self.__commnet_list = []
    
    @property
    def make_detail(self): return [self.__name, self.id, self.__price, self.__description]

    @property
    def get_comment_dict(self):
        res = []
        for i in self.__commnet_list:
            res.append(i.convert_to_dict)
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
    
    def add_comment(self, comment : Comment):
        res = ""
        if isinstance(comment, Comment):
            self.__commnet_list.append(comment)
            res = "Done"
        return res
#endregion

#region Coupon
class Coupon(Object):
    def __init__(self, id):
        super().__init__(id)

#endregion

#region Categories
class Categories:

    #collect product as id
    def __init__(self,name):
        self.__name = name
        self.__products_id = []

    @property
    def name(self):
        return self.__name
    
    @property
    def products(self):
        return self.__products_id
    
    def add_product(self, product_id : str):
        if isinstance(product_id, list):
            self.__products_id.extend(product_id)
        else:
            self.__products_id.append(product_id)
        
#endregion
#region Address
class Address:
    #district = เขต
    #province  = ตำบล
    #zipcode = ไปรษณีย์
    def __init__(self, district, province, zip_code, phone_number):
        self.__district = district
        self.__province = province
        self.__zip_code = zip_code
        self.__phone_number = phone_number

    def __str__(self):
        return {
            "District" : self.__district,
            "Province" : self.__province,
            "Zip Code" : self.__zip_code,
            "Phone Number" : self.__phone_number
        }
    
    @property
    def district(self):
        return self.__district
    
    @property
    def province(self):
        return self.__province
    
    @property
    def zip_code(self):
        return self.__zip_code
    
    @property
    def phone_number(self):
        return self.__phone_number
#endregion
#region Account
class Account(Object):
    __address_list : Address
    def __init__(self, id = "", name = "", username = "", password ="", money = 0 ,image = "",market = None):
        super().__init__(id)
         #use for login
        self.__name = name
        self.__password = password

        self.__username = username
        self.__image = image
        self.__money = money
        self.__market = market
        self.__address_list = []


class Customer(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 0 ,image = "",market = None):
        super().__init__(id, name,username, password, money, image, market)
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
    def __init__(self, customer_id, product_id):
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__date = datetime.now()

    def __str__(self):
        return {
            "customer_id" : self.__customer_id,
            "product_id" : self.__product_id,
            "date" : self.__date
        }
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def date(self):
        return self.__date
#endregion

    

#region cart
class Cart:
    def __init__(self):
        self.__product_List = []

    def remove_product(self, product : Product):
        for i in self.__product_List:
            if i.Equal(product.id):
                self.__product_List.remove(i)
                return {
                    "success" : True,
                    "message" : "Remove Complete"
                }
            
        return  {
            "success" : False,
            "message" : "Product Not found"
        }

    @property
    def product_list(self):
        return self.__product_List
    
    def add_product(self, product : Product):
        self.product_list.append(product)
        return "success"

#endregion

         

#region Market
class Market():
    __account_list : Account
    __product_list : Product
    __coupon_list : Coupon
    __category_list : Categories

    def __init__(self):
        self.__account_list = []
        self.__product_list = []
        self.__coupon_list = []
        self.__category_list = []
        #make it private nah
        self.__exist_id = []

    @property
    def account_list(self):
        return self.__account_list
    
    @property
    def product_list(self):
        return self.__product_list
    
    @property
    def coupon_list(self):
        return self.__coupon_list
    
    def generate_id(self):
        return ""
    
    def add_account(self, account : Account):
        self.__account_list.append(account)
        
    def add_product(self, product : Product):
        if isinstance(product, Product):
            self.__product_list.append(product)

            category = self.get_categories(product.category)
            if(category != None):
                category.add_product(product.id)
            else:
                newCate = self.add_category
            return "Done"

    def add_category(self, name):
        self.__category_list.append(Categories(name))
    
    def add_category(self, name, product : Product):
        newCate = Categories(name)
        newCate.add_product(product)
        self.__category_list.append(newCate)
        return newCate
        
    def purchase(self, user_id, address, coupon, money):
        return {
            "success" : True
        }
    
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
    
    def get_categories(self, name):
        for i in self.__category_list:
            if(name == i.name):
                return i
        return None
    
    
    def get_product_detail(self, product): return product.detail
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        return self.get_product_detail(product)
    
    def search(self, name):
        return [p for p in self.__product_list if name.lower() in p.name.lower()]
    
    def search(self, name , tag):
        return

#endregion
def create_json(list1, list2):
    res = {}
    for i in range(len(list1)):
        res[list1[i]] = list2[i]
    return res

def set_up():
    m = Market()
    user1 = Customer(name="Opor", market = m)
    p = [Product("Book", 
                 1,
                 200,
                 "Book that everyone can read",
                 "https://cdn-icons-png.flaticon.com/512/8832/8832880.png",
                 "Book"),   
         Product("Book more cost",
                 2,
                 250,
                 "Book that rich guy can read",
                 "https://pngimg.com/uploads/book/book_PNG2114.png",
                 "Book")
        ]
    c = [Comment("Bruno", "This product is so good", 5)]
    for i in p:
        m.add_product(i)
    p[0].add_comment(c[0])
    return m