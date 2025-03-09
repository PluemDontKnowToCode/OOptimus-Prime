import enum
from datetime import *
import json
import os
import re
main_path = os.path.dirname(__file__)
file_path = os.path.join(main_path, '../jsonData')

from backend.Account import *
from backend.Address import *
from backend.Admin import *
from backend.Cart import *
from backend.Categories import *
from backend.Comment import *
from backend.Coupon import *
from backend.Customer import *
from backend.DiscountProduct import *
from backend.Object import *
from backend.Product import *
from backend.Seller import *
from backend.StackItem import *
from backend.Transaction import *
from backend.RequestedProduct import *

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
        self.__requested_list = []
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
    
    @property
    def requested_list(self):
        return self.__requested_list
    
    def update_current_user(self, user : Account):
        if isinstance(user , Account):
            self.__current_user = user
        
    def generate_product_id(self):
        temp_id = []

        for i in self.product_list:
            temp_id.append(i.id)

        a = sorted(temp_id)
        number = int(re.search(r'P(\d+)', a).group(1))
        number += 1
        new_id = f"P{number:06d}"
        print(f"new Id : {new_id}")
        return new_id
    
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
    def add_coupon(self, coupon : Coupon):
        if(isinstance(coupon, Coupon)):
            self.__coupon_list.append(coupon)

    def add_product_to_cart(self, p_id, u_id, amount):
        p1 = self.get_product(p_id)
        if not p1: return
        for i in self.__customer_list:
            if i.equal(u_id): i.add_to_cart(p1, amount); return "Product was added to cart"

    def add_category(self, name):
        self.__category_list.append(Categories(name))
    
    def add_category(self, name, product : Product):
        if(isinstance(product , Product)):
            newCate = Categories(name)
            newCate.add_product(product)
            self.__category_list.append(newCate)
    
    def add_requested(self, request):
        if(isinstance(request, RequestedProduct)):
            self.__requested_list.append(request)
            return "Success"

    def add_comment_to_product(self, p_id, comment):
        # if isinstance(comment, Comment): return "Type invalid"
        p = self.get_product(p_id)
        # if not p: return "Not find product"
        p.add_comment(comment)
        # return "Done"
    
    def delete_coupon(self, id):
        for i in self.__coupon_list:
            if i.id == id:
                self.__coupon_list.remove(i)
                return "Remove Success"
        return "Not Found"
        
    def purchase(self, user_id, coupon = None):
        customer = self.get_account(user_id)
        if(customer == None):
            return "User Not Found"
            
        cart = customer.cart
        
        price = cart.calculate_price()
        
        if(coupon != None):
            if(self.get_coupon(coupon.id)):
                if(coupon.check_condition(cart)):
                    return "Coupon Condition Not Met"
                discountPercent = self.get_coupon(coupon.id).discount_percent
                price -= price * discountPercent
            else:
                return "Coupon Not Found"
                
        if(price > customer.money):
            return "Not Enough Money"
        
        for i in cart.get_cart_item:
            i.product.update_stock(-1 * i.amount)

        customer.update_money(price)
        customer.clear_cart()

        for p in cart.product_list:
            customer.add_transaction(Transaction(p.id))
        
        return "success"
    
    def get_account(self, user_id): 
        for i in self.__customer_list + self.__seller_list + self.__admin_list:
            # print(i.name)
            if i.equal(user_id):
                return i
        return None
    
    def get_product(self, product_id):
        for i in self.__product_list:
            if i.equal(product_id): 
                return i
        return None
    def get_coupon(self, coupon_id):
        for i in self.__coupon_list:
            if i.equal(coupon_id): 
                return i
        return None
    
    def get_categories(self, name):
        for i in self.__category_list:
            if(name == i.name):
                return i
        return None

    def get_customer_cart(self,customer_id):
        customer = self.get_account(customer_id)
        if isinstance(customer, Customer):
            return customer.cart
    
    def get_customer_cart_product(self, customer):
        res = []
        # print(customer.cart_product)
        for p in customer.cart_items:
            res.append(p)
        return res
    
    def get_requested(self, id):
        if isinstance(id, str):
            for i in self.requested_list:
                if i.product.id == id:
                    return i
                
        return None
    
    def get_product_detail(self, product): return product.detail
    
    def get_product_image(self, p_id):
        return self.get_product(p_id).image
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        return self.get_product_detail(product)
    
    def search(self, name):
        return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    # def search(self, name , tag):
    #     return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    # def search(self, tag):
    #     return
    
    @property
    def update_product(self):
        pjson = open(file_path + '/Product.json', 'w')
        t1 = """{\n\t\t"data" : [\n\t\t\t"""
        pass
    
    def clear_current_account(self):
        self.__current_user = None
    
    def verify_user(self, name, password, role):
        list1 = None
        if "admin" in name.lower(): list1 = self.__admin_list
        elif role == "customer": list1 = self.__customer_list
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
            pd = Product(i, market1)
            res.append(pd)
    return res

def get_all_account():
    res = []
    with open(file_path + '/Account.json', "r") as file01:
        account_json = json.loads(file01.read())
        for i in account_json["data"]:
            ac = Customer(i, market1)
            res.append(ac)
    with open(file_path + '/Admin.json', "r") as file01:
        account_json = json.loads(file01.read())
        for i in account_json["data"]:
            ac = Admin(i, market1)
            res.append(ac)
    with open(file_path + '/Seller.json', "r") as file01:
        account_json = json.loads(file01.read())
        for i in account_json["data"]:
            ac = Seller(i, market1)
            res.append(ac)
    return res


def get_all_coupon():
    res = []
    with open(file_path + '/Coupon.json', "r") as file01:
        coupon_json = json.loads(file01.read())
        for i in coupon_json["data"]:
            cp = Coupon(i["id"],i['discount_percent'], i['less_amount'], i['product_count'], i['start_time'], i['end_time'])
            res.append(cp)
    return res

def get_all_UnImproveProduct():
    res = []
    with open(file_path + '/UnImproveProduct.json', "r") as file01:
        product_json = json.loads(file01.read())
        for i in product_json["data"]:
            # print(i)
            pd = Product(i, market1)
            seller = market1.get_account(i["seller"])
            rp = RequestedProduct(pd, seller)
            res.append(rp)
    return res

market1 = Market()
for i in get_all_account():
    market1.add_account(i)

for i in get_all_product():
    market1.add_product(i)

for i in get_all_coupon():
    market1.add_coupon(i)

for i in get_all_UnImproveProduct():
    market1.add_requested(i)

market1.update_current_user(market1.get_account("A000001"))

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