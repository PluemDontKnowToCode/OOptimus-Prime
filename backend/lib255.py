import enum
import datetime
import json
import os
main_path = os.path.dirname(__file__)
file_path = os.path.join(main_path, '../jsonData')
    
class Object:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        # print("Sending my id")
        return self.__id

    def set_id(self, id1): self.__id = id1
    
    def Equal(self, id):
        return self.__id == id

#region Comment
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
#endregion
#region Product
class Product(Object):

    #image is list na
    def __init__(self, name = '', id = '', price = 0, description = '', img1 = '', category = ''):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__img = img1
        self.__category = category
        self.__comment_list = []
        super().__init__(id)
    
    def __init__(self, d: dict):
        self.__name = d['name']
        self.__price = d['price']
        self.__description = d['description']
        self.__img = d['img']
        self.__category = d['category']
        clist = []
        for i in d['comment']:
            c = Comment(i['name'], i['text'], i['star'])
            clist.append(c)
        self.__comment_list = clist
        super().__init__(d['id'])
    
    @property
    def make_detail(self): return [self.__name, self.__price, self.__description]

    @property
    def get_comment_dict(self):
        res = []
        for i in self.__comment_list:
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
    
    def to_json(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "price" : self.price,
            "description" : self.description,
            "img" : self.image,
            "category" : self.category,
            "comment" : [i.convert_to_dict for i in self.__comment_list]
        }
        
    def add_comment(self, comment : Comment):
        res = ""
        if isinstance(comment, Comment):
            self.__comment_list.append(comment)
            res = "Done"
        return res
    
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
#endregion

#region Coupon
class Coupon(Object):
    def __init__(self, id,name,description, discount_percent,less_amount : float,product_count = 0,product_accord = []):
        super().__init__(id)
        self.__name = name
        self.__description = description
        self.__discount_percent = discount_percent
        self.__less_amount = less_amount
        self.__product_count = product_count
        self.__product_accord = product_accord
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
            "name":self.__name
        }
#endregion

#region Categories
class Categories:

    #collect product as id
    def __init__(self,name):
        self.__name = name
        self.__product = []

    @property
    def name(self):
        return self.__name
    
    @property
    def products(self):
        return self.__product
    
    def add_product(self, product : Product):
        if isinstance(product, list):
            self.__product.extend(product)
        else:
            self.__product.append(product)
        return {
            "success" : True
        }   
    def remove_product(self, product : Product):
        self.__product.remove(product)
        return {
            "success" : True
        }
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
        self.__address_list = d['address']
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

class Customer(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 0 ,image = "",market = None):
        super().__init__(id, name,username, password, money, image, market)
        self.__cart = Cart()
        self.__transaction = []
        self.__coupon_list = []
        
    @property
    def cart(self):
        return self.__cart
    
    @property
    def cart_product(self):
        return self.__cart.product_list
    
    def add_transaction(self,product_id,datetime):
        self.__transaction.append(Transaction(id,product_id,datetime))
        return
    
    def update_money(self, amount):
        self.__money += amount
        return
        
    def view_product_detail(self, product_id): return self.__market.view_product_detail(product_id)

    def to_json(self):
        return {
            "name" : super().name,
            "username" : super().username,
            "image" : super().image,
            "money" : super().money,
            "address" : super().address_list,
            "cart" : self.cart,
            "transaction" : self.__transaction,
            "coupon" : self.__coupon_list
        }

class Seller(Account):
    def __init__(self, id):
        super().__init__(id)
        self.__selling_product = []
    
    def create_product(self, product : Product):
        self.__selling_product.append(product)

    def delete_product(self, product : Product):
        self.__selling_product.remove(product)

    def delete_product(self, product_id : str):
        product = super().market.get_product(product_id)
        self.__selling_product.remove(product)

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

    def calculate_price(self):
        return {   
            "price" : sum(item.price for item in self.__product_List),
            "len" : len(self.__product_List) 
        }
        
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
                category.add_product(product)
            else:
                self.add_category(product.category ,product)
            return "Done"

    def add_category(self, name):
        self.__category_list.append(Categories(name))
    
    def add_category(self, name, product : Product):
        newCate = Categories(name)
        newCate.add_product(product)
        self.__category_list.append(newCate)
        
    def purchase(self, user_id, address, coupon, money):
        return {
            "success" : True
        }
    
    def get_account(self, user_id): 
        for i in self.__account_list:
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

    def get_customer_cart(self,customer_id):
        customer = self.get_account(customer_id)
        if(customer == None):
            return {
                "success" : False,
                "message" : "User Not Found"
            }
        existProduct = []
        for c in customer.cart_product:
            if(self.get_product(c.id)):
                existProduct.append(c.to_json())
        return {
            "success" : "True",
            "data" : existProduct
        }   
    def get_product_detail(self, product): return product.detail
    
    def get_product_image(self, p_id):
        return self.get_product(p_id).image
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        return self.get_product_detail(product)
    
    def search(self, name):
        return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    def search(self, name , tag):
        return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    def search(self,tag):
        return
    
    @property
    def update_product(self):
        pjson = open(file_path + '/Product.json', 'w')
        t1 = """{\n\t\t"data" : [\n\t\t\t"""
        pass
        


#endregion

def create_json(list1, list2):
    res = {}
    for i in range(len(list1)):
        res[list1[i]] = list2[i]
    return res

def set_up():
    m = Market()
    return m

def get_all_product():
    res = []
    with open(file_path + '/Product.json', "r") as file01:
        product_json = json.loads(file01.read())
        for i in product_json["data"]:
            pd = Product(i)
        
            res.append(pd)
    return res
def get_all_account():
    res = []
    with open(file_path + '/Account.json', "r") as file01:
        account_json = json.loads(file01.read())
        for i in account_json["data"]:
            ac = Account(i)
        
            res.append(ac)
    return res

market1 = Market()
for i in get_all_product():
    market1.add_product(i)