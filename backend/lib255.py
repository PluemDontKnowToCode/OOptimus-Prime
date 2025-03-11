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
from backend.Category import *
from backend.Comment import *
from backend.Coupon import *
from backend.Customer import *
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
        
        self.__selected_category = None
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
    
    @property
    def category_list(self):
        return self.__category_list
    
    @property
    def selected_category(self):
        return self.__selected_category
    
    def update_selected_category(self, category):
        if isinstance(category, Category):
            self.__selected_category = category
            return "Update Category Success"
        return "Update Category Failed"
    
    def update_current_user(self, user : Account):
        if isinstance(user , Account):
            self.__current_user = user

    def change_username(self, new_name):
        if isinstance(self.__current_user, Account):
            self.__current_user.rename(new_name)
        return None
        
    def generate_id(self, state):
        var = [[self.__product_list, 'P'], [self.__customer_list, 'A'], [self.__seller_list, 'S'], [self.__admin_list, 'M'], [self.__coupon_list, 'C']]
        now_list, now_char = var[state]
        temp_id = []

        for i in now_list:
            temp_str: str = i.id
            temp_id.append(temp_str.removeprefix(now_char))

        temp_id.sort()
        number = int(temp_id[-1]) + 1
        new_id = f"{now_char}{number}"
        print(f"NEW ID: {new_id}")
        return new_id
    
    def add_account(self, account):
        if isinstance(account, Customer): self.__customer_list.append(account)
        elif isinstance(account, Seller): self.__seller_list.append(account)
        elif isinstance(account, Admin): self.__admin_list.append(account)
        
    def add_product(self, product : Product):
        if isinstance(product, Product):
            self.__product_list.append(product)

            category = self.get_category(product.category)
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
        self.__category_list.append(Category(name))
    
    def add_category(self, name, product : Product):
        if(isinstance(product , Product)):
            newCate = Category(name)
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
        
    def add_coupon_to_account(self, coupon_id):
        res = self.is_have_coupon(coupon_id)
        if isinstance(res, str): return
        if not res:
            self.__current_user.add_coupon(self.get_coupon(coupon_id))
            
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

        stack_item_list = cart.get_cart_item
        print(f"GET stack item {stack_item_list}")
        
        price = cart.calculate_price()
        
        if(coupon != None):
            if(self.get_coupon(coupon.id)):
                if not (coupon.check_condition(cart)):
                    return "Coupon Condition Not Met"
                discountPercent = self.get_coupon(coupon.id).discount_percent
                price -= price * discountPercent
            else:
                return "Coupon Not Found"
                
        if(price > customer.money):
            return "Not Enough Money"

        stack_product = cart.product_list
        amount =  cart.each_stack_amount
        trans1 = Transaction(stack_product, amount)
        customer.add_transaction(trans1)
        
        if coupon: customer.delete_coupon(coupon)

        for i in cart.get_cart_item:
            i.product.update_stock(-1 * i.amount)

        customer.update_money(price)
        customer.clear_cart()
        
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
    
    def get_category(self, name):
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
        res = None
        if self.get_product(p_id): res = self.get_product(p_id).image
        elif self.get_requested(p_id): res = self.get_requested(p_id).image
        return res
    
    def is_product_approve(self, p_id):
        return isinstance(self.get_product(p_id), Product)
    
    def get_requested_image(self, p_id):
        return self.get_requested(p_id).product.image
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        if not product:
            product = self.get_requested(product_id).product
        return self.get_product_detail(product)
    
    def search(self, name):
        return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    def get_transaction_list(self):
        if not self.__current_user: return
        if isinstance(self.__current_user, Customer): 
            return self.__current_user.get_transaction_list()
    
    # def search(self, name , tag):
    #     return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    #search by category
    def search_by_category(self, tag_name):
        selected = self.get_category(tag_name)
        if selected:
            return selected.get_product_list()
        return "Not Found"
    
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
    
    def is_have_coupon(self, coupon_id):
        acc = self.__current_user
        if isinstance(acc, Customer):
            if len(acc.coupon_list) == 0: return False
            if acc.is_have_coupon(coupon_id): return True
            return False
        return "Invalid"
        


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
        for d in product_json["data"]:
            # print(i)
            temp_c = []
            for i in d['comment']:
                acc = market1.get_account(i['owner_id'])
                # print(f"{acc} {i['owner_id']}")
                c = Comment(acc.name, i['text'], i['star'], i['owner_id'])
                temp_c.append(c)
            pd = Product(name = d['name'],id = d['id'],price = d['price'], description = d['description'], img1 = d['img'], category = d['category'],stock =  d['stock'],comment_list = temp_c,market =  market1)
            res.append(pd)
    return res
def get_all_customer():
    res = []
    with open(file_path + '/Account.json', "r") as file01:
        account_json = json.loads(file01.read())
        for d in account_json["data"]:
            temp = []
            temp_coupon = []
            for i in d['address']:
                temp.append(Address(i['district'], i['province'], i['zip_code'], i['phone']))
            for i in d['coupon']:
                start_time = datetime.strptime(i['start_time'], "%Y-%m-%d")
                end_time = datetime.strptime(i['end_time'], "%Y-%m-%d")
                temp_coupon.append(Coupon(i["id"],i['discount_percent'], i['less_amount'], i['product_count'],start_time, end_time))

            ac = Customer(d['id'],d['name'],d['username'],d['password'],d['money'],temp,d['image'],temp_coupon, market1)
            res.append(ac)
    return res

def get_all_admin():
    res = []
    with open(file_path + '/Admin.json', "r") as file01:
        account_json = json.loads(file01.read())
        for d in account_json["data"]:
            temp = []
            for i in d['address']:
                temp.append(Address(i['district'], i['province'], i['zip_code'], i['phone']))
            ac = Admin(d['id'],d['name'],d['username'],d['password'],d['money'],temp, d['image'], market1)
            res.append(ac)
    return res

def get_all_seller():
    res = []
    with open(file_path + '/Seller.json', "r") as file01:
        account_json = json.loads(file01.read())
        for d in account_json["data"]:
            temp_s = []
            temp_i = []
            for j in d["product"]:
                temp_s.append(market1.get_product(j["id"]))
            ac = Seller(d['id'],d['name'],d['username'],d['password'],d['money'],temp_s,d['image'], market = market1)
            res.append(ac)
    return res


def get_all_coupon():
    res = []
    with open(file_path + '/Coupon.json', "r") as file01:
        coupon_json = json.loads(file01.read())
        for i in coupon_json["data"]:
            start_time = datetime.strptime(i['start_time'], "%Y-%m-%d")
            end_time = datetime.strptime(i['end_time'], "%Y-%m-%d")
            cp = Coupon(i["id"],i['discount_percent'], i['less_amount'], i['product_count'], start_time, end_time)
            res.append(cp)
    return res

def get_all_UnImproveProduct():
    res = []
    with open(file_path + '/UnImproveProduct.json', "r") as file01:
        product_json = json.loads(file01.read())
        for d in product_json["data"]:
            # print(i)
            temp_c = []
            pd = Product(name = d['name'],id = d['id'],price = d['price'], description = d['description'], img1 = d['img'], category = d['category'],stock =  d['stock'],comment_list = temp_c,market =  market1)
            seller = market1.get_account(d["seller"])
            rp = RequestedProduct(pd, seller)
            res.append(rp)
    return res

market1 = Market()


for i in get_all_customer():
    market1.add_account(i)

for i in get_all_product():
    market1.add_product(i)

for i in get_all_seller():
    market1.add_account(i)

for i in get_all_admin():
    market1.add_account(i)

for i in get_all_UnImproveProduct():
    market1.add_requested(i)

for i in get_all_coupon():
    market1.add_coupon(i)


market1.update_current_user(market1.get_account('A000001'))

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