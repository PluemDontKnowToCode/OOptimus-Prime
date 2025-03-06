import enum
from datetime import *
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
    def __init__(self, name, text, star : int, new_id):
        self.__name = name
        self.__text = text
        self.__star = star
        self.__user_id = new_id
    
    def to_json(self):
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
    def __init__(self, name = '', id = '', price = 0, description = '', img1 = '', category = '', stock = 0):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__img = img1
        self.__category = category
        self.__comment_list = []
        self.__stock = stock
        super().__init__(id)
    
    def __init__(self, d: dict):
        self.__name = d['name']
        self.__price = d['price']
        self.__description = d['description']
        self.__img = d['img']
        self.__category = d['category']
        self.__stock = d['stock']
        clist = []
        
        # print(market1.account_list) 
        for i in d['comment']:
            acc = market1.get_account(i['owner_id'])
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
    def __init__(self, id, discount_percent,less_amount : float,product_count = 0, start_time = datetime.now(), duration = 0):
        super().__init__(id)
        self.__discount_percent = discount_percent
        self.__less_amount = less_amount
        self.__product_count = product_count
        self.__start_time = start_time
        self.__end_time = start_time + timedelta(days = duration)
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
            "discount_percent" : self.__discount_percent,
            "less_amount" : self.__less_amount,
            "product_count" : self.__product_count,
            "start_time" : self.__start_time,
            "end_time" : self.__end_time
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
        return "success"
    def remove_product(self, product : Product):
        self.__product.remove(product)
        return "success"
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

    def to_json(self):
        return {
            "district" : self.__district,
            "province" : self.__province,
            "zip_code" : self.__zip_code,
            "phone" : self.__phone_number
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
        

class Customer(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 0 ,image = "",market = None):
        super().__init__(id, name,username, password, money, image, market)
        self.__cart = Cart()
        self.__transaction = []
        self.__coupon_list = []
    
    def __init__(self, d: dict, market = None):
        super().__init__(d, market)
        self.__cart = Cart() 
        self.__coupon_list = []
        if(d["transaction"] != None): 
            self.__transaction = d['transaction']
    @property
    def cart(self):
        return self.__cart
    @property
    def coupon_list(self):
        return self.__coupon_list
    @property
    def cart_product(self):
        # print(f"Cart_product: {self.__cart.product_list}")
        return self.__cart.product_list
    
    @property
    def cart_items(self): return self.__cart.get_cart_item
    
    def get_coupon(self):
        res = []
        for i in self.coupon_list:
            res.append(i.to_json())
        return res
        
    def add_coupon(self, coupon : Coupon):
        self.__coupon_list.append(coupon)
        return "Add Complete"
        
    
    def add_to_cart(self, product : Product, amount):
        return self.__cart.add_item(product, amount)
        
    def clear_cart(self):
        self.__cart.clear()

    def add_transaction(self,product_id):
        self.__transaction.append(Transaction(self.id,product_id))
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

    def __init__(self, d: dict, market = None):
        super().__init__(d, market)

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

    def __init__(self, d: dict, market = None):
        super().__init__(d, market)
#endregion
#region Transaction
class Transaction():
    def __init__(self, product_id):
        self.__product_id = product_id
        self.__date = datetime.now()

    def to_json(self):
        return {
            "customer_id" : self.__customer_id,
            "product_id" : self.__product_id,
            "date" : self.__date
        }
    
    
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def date(self):
        return self.__date
#endregion

class StackItem:
    def __init__(self, product, amount = 1):
        self.__product = product
        self.__amount = self.validate_amount(amount)
        
    @property
    def inc_item(self): 
        if self.__amount < self.__product.stock: self.__amount += 1

    @property
    def dec_item(self): 
        if self.__amount >= 0: self.__amount -= 1

    @property
    def product(self): return self.__product

    def validate_amount(self, a1):
        if a1 >= self.__product.stock:
            return self.__product.stock
        elif a1 <= 0: 
            return None
        else:
            return a1
    
    @property
    def amount(self): return self.__amount
    
    
    def set_amount(self, a1):
        self.__amount = self.validate_amount(a1)
    @property
    def to_json(self): return { self.__product: self.__amount }

    def is_me(self, product): return product == self.__product

    @property
    def price(self): return self.__product.price * self.__amount

#region cart
class Cart:
    def __init__(self):
        self.__cart_item_list = []

    @property
    def size(self):
        res = 0
        for i in self.__cart_item_list:
            res += i.amount
        return res
    
    @property
    def get_cart_item(self): return self.__cart_item_list

    @property
    def product_list(self): return [i.product for i in self.__cart_item_list]
    
    @property
    def get_product(self):
        res = []
        for i in self.__cart_item_list:
            dict1 = i.product.to_json()
            dict1.update({"amount": i.amount})
            res.append(dict1)
        return res

    def remove_item(self, product : Product):
        for i in self.__cart_item_list:
            if i.product.Equal(product.id):
                self.__cart_item_list.remove(i)
                return "Remove Complete"
        return "Product Not found"
        
    def clear(self):
        self.__cart_item_list.clear()
        return "Clear Complete"
        
    def add_item(self, product : Product, amount):
        print(f"type, amount: {type(product)}, {amount}")
        if not isinstance(product, Product): return "False"
        if product in self.product_list:
            for i in self.__cart_item_list:
                if i.is_me(product): i.set_amount(amount)
                break
        else:
            self.__cart_item_list.append(StackItem(product, amount))
        return "Add Complete"
        
    def calculate_price(self):
        return {   
            "price" : sum(item.price for item in self.__cart_item_list),
            "len" : self.size 
        }
        
#endregion

         

#region Market
class Market():

    def __init__(self):
        self.__current_user = None
        self.__seller_list = []
        self.__customer_list = []
        self.__product_list = []
        self.__admin_list = []
        self.__coupon_list = []
        self.__category_list = []
        #make it private nah
        self.__exist_id = []

    @property
    def account_list(self):
        return self.__seller_list + self.__customer_list
    
    @property
    def product_list(self):
        return self.__product_list
    
    @property
    def coupon_list(self):
        return self.__coupon_list
    @property
    def current_account(self):
        return self.__current_user
    
    def update_current_user(self, user : Account):
        self.__current_user = user
        
    def generate_id(self):
        return ""
    
    def add_account(self, account):
        if isinstance(account, Customer): self.__customer_list.append(account)
        elif isinstance(account, Seller): self.__seller_list.append(account)
        elif isinstance(account, Admin): self.__admin_list.append(account)
        
    def add_product(self, product : Product):
        if isinstance(product, Product):
            self.__product_list.append(product)

            category = self.get_categories(product.category)
            if(category != None):
                category.add_product(product)
            else:
                self.add_category(product.category ,product)
            return "Done"
        
    def add_product_to_cart(self, p_id, u_id, amount):
        p1 = self.get_product(p_id)
        if not p1: return
        for i in self.__customer_list:
            if i.Equal(u_id): i.add_to_cart(p1, amount); return "Product was added to cart"

    def add_category(self, name):
        self.__category_list.append(Categories(name))
    
    def add_category(self, name, product : Product):
        newCate = Categories(name)
        newCate.add_product(product)
        self.__category_list.append(newCate)

    def add_comment_to_product(self, p_id, comment):
        # if isinstance(comment, Comment): return "Type invalid"
        p = self.get_product(p_id)
        # if not p: return "Not find product"
        p.add_comment(comment)
        # return "Done"
        
        
    def purchase(self, user_id, address, coupon):
        customer = self.get_account(user_id)
        if(customer == None):
            return "User Not Found"
            
        cart = customer.cart

        price = 0
        for p in cart.product_list:
            price += p.price

        if(coupon != None):
            if(self.get_coupon(coupon)):
                discountPercent = self.get_coupon(coupon).discount_percent
                price -= price * discountPercent
            else:
                return "Coupon Not Found"
                
        if(price > customer.money):
            return "Not Enough Money"
            
        customer.update_money(price)
        customer.clear_cart()

        for p in cart.product_list:
            customer.add_transaction(Transaction(p.id))
        
        return "success"
    
    def get_account(self, user_id): 
        for i in self.__customer_list + self.__seller_list:
            # print(i.name)
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

    def get_customer_cart(self,customer):
        return customer.cart
    
    def get_customer_cart_product(self, customer):
        res = []
        # print(customer.cart_product)
        for p in customer.cart_items:
            res.append(p)
        return res
    
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
    
    def search(self, tag):
        return
    
    @property
    def update_product(self):
        pjson = open(file_path + '/Product.json', 'w')
        t1 = """{\n\t\t"data" : [\n\t\t\t"""
        pass
    
    def verify_user(self, name, password, role):
        list1 = None
        if role == "customer": list1 = self.__customer_list
        elif role == "seller": list1 = self.__seller_list
        else: return list1
        
        for i in list1:
            lean = i.self_verify(name, password)
            if lean: return i
        return None
        


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
            # print(i)
            pd = Product(i)
            res.append(pd)
    return res

def get_all_account():
    res = []
    with open(file_path + '/Account.json', "r") as file01:
        account_json = json.loads(file01.read())
        for i in account_json["data"]:
            if(i["role"] == "Customer"):
                ac = Customer(i, market1)
            elif(i["role"] == "Seller"):
                ac = Seller(i,market1)
            elif(i["role"] == "Admin"):
                ac = Admin(i,market1)
            res.append(ac)
    return res


def get_all_coupon():
    res = []
    with open(file_path + '/Coupon.json', "r") as file01:
        coupon_json = json.loads(file01.read())
        for i in coupon_json["data"]:
            cp = Coupon(i)
            res.append(cp)
    return res

market1 = Market()
for i in get_all_account():
    market1.add_account(i)
for i in get_all_product():
    market1.add_product(i)
    
# market1.update_current_user(market1.get_account("A000001"))

# p = market1.get_product("P000001")
# market1.current_account.cart.add_item(p, 1)

# for i in get_all_account():
#     market1.add_account(i)
    
# for i, j in vars(market1).items():
#     print(i, end = "   ")
#     if isinstance(j, list):
#         for z in j:
#             for k, v in vars(z).items():
#                 print(k, v)
#     else: print(j)
    
# c1 = Customer(id="C000001", name="Teerawee", username="teerawee", password="1234")
# print(c1.coupon_list)