from fasthtml.common import *
from fasthtml.common import *
import enum
from datetime import *
import enum
import json
import os
import enum
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

    @property
    def account_list(self):
        return self.__seller_list + self.__customer_list + self.__admin_list
    
    @property
    def product_list(self):
        return self.__product_list
    
    @property
    def coupon_list(self):
        return self.__coupon_list
    @property
    def current_user(self):
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
    
    def view_product_detail(self, product_id):
        product = self.get_product(product_id)
        if not product:
            product = self.get_requested(product_id).product
        return self.get_product_detail(product)
    
    def search(self, name):
        return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    def get_user_transaction_list(self):
        if not self.__current_user: return
        if isinstance(self.__current_user, Customer): 
            return self.__current_user.get_transaction_list()
    def generate_id(self, state):
        var = [[self.__product_list, 'P'], [self.__customer_list, 'A'], [self.__seller_list, 'S'], [self.__admin_list, 'M'], [self.__coupon_list, 'C']]
        now_list, now_char = var[state]
        temp_id = []
        for i in now_list:
            temp_str: str = i.id
            temp_id.append(temp_str.removeprefix(now_char))
            
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
        
    def add_coupon_to_current_user(self, coupon_id):
        res = self.is_current_user_have_coupon(coupon_id)
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
        
        price = cart.calculate_price()
        
        if(coupon != None):
            if(self.get_coupon(coupon.id) and coupon.id == self.current_user.selected_coupon.id):
                if not (coupon.check_condition(cart)):
                    return "Coupon Condition Not Met"
                discountPercent = coupon.discount_percent
                price -= price * discountPercent
            else:
                customer.delete_coupon(coupon)
                return "Coupon Not Found"
                
        if(price > customer.money):
            return "Not Enough Money"

        stack_product = cart.product_list
        amount =  cart.each_stack_amount
        trans1 = Transaction(stack_product, amount)
        customer.add_transaction(trans1)
        
        if coupon: 
             customer.update_selected_coupon(None)
             customer.delete_coupon(coupon)

        for i in cart.get_cart_item:
            i.product.update_stock(-1 * i.amount)

        customer.update_money(price)
        customer.clear_cart()
        
        return "success"
    # def search(self, name , tag):
    #     return [p.to_json() for p in self.__product_list if name.lower() in p.name.lower()]
    
    #search by category
    def search_by_category(self, category):
        self.update_selected_category(category)
        if category:
            return category.get_product_list()
        return "Not Found"

    def get_list_for_verify_user(self, name, role):
        res = None
        if "admin" in name.lower(): res = self.__admin_list
        elif role == "customer": res = self.__customer_list
        elif role == "seller": res = self.__seller_list
        return res

    def request_to_self_verify(self, account, name, password):
        return account.self_verify(name, password)
    
    def verify_user(self, name, password, role):
        list1 = self.get_list_for_verify_user(name, role)
        
        for i in list1:
            if self.request_to_self_verify(i, name, password): return i
        return None
    
    def is_current_user_have_coupon(self, coupon_id):
        acc = self.__current_user
        if isinstance(acc, Customer):
            if len(acc.coupon_list) == 0: return False
            if acc.is_have_coupon(coupon_id): return True
            return False
        return "Invalid"

    def validate_login(self, name: str, password: str, role: str):
        acc = self.verify_user(name, password, role)
        if not acc: return Redirect('/login')
        self.update_current_user(acc)
        return Redirect('/')
     
    def validate_register(self,name : str, password : str, r_password : str, role : str):
        if(password != r_password):
            return 'error'
        if self.is_user_exist(name, password): return "error"
        if role == "customer":
            new_account = Customer(id=self.generate_id(1),name=  name,username= name,password= password, money =10000, market= market1)
        elif role == "seller":
            new_account = Seller(id=self.generate_id(2),name=  name,username= name,password= password, money =10000, market= market1)
            
        self.update_current_user(new_account)
        self.add_account(new_account)
        return "success"

    def is_user_exist(self, username ,password):
        for i in self.account_list:
            if i.username == username and i.password == password:
                return True
        return False
    
    def update_user_image(self, new_image_url):
        if isinstance(self.current_user, Customer):
            self.current_user.image = new_image_url
            # Save the updated account information to the database or file
            self.save_account(self.current_user)

    def save_account(self, account):
        # Implement the logic to save the account information to the database or file
        pass

    def add_user_address(self, district, province, zip_code, phone_number):
        if isinstance(self.current_user, Customer):
            # Check if any field is empty
            if not district or not province or not zip_code or not phone_number:
                return 'All fields are required.'
            
            # Check if the address already exists
            for address in self.current_user.address_list:
                if address.district == district and address.province == province and address.zip_code == zip_code and address.phone_number == phone_number:
                    return 'Address already exists.'
            
            new_address = Address(district=district, province=province, zip_code=zip_code, phone_number=phone_number)
            self.current_user.address_list.append(new_address)
            return 'success'

    def delete_address(self, district):
        self.current_user.address_list[:] = [address for address in self.current_user.address_list if address.district != district]
    
    def update_address(self, old_district, new_district, new_province, new_zip_code, new_phone_number):
        for address in self.current_user.address_list:
            if address.district == old_district:
                address.district = new_district
                address.province = new_province
                address.zip_code = new_zip_code
                address.phone_number = new_phone_number
                break

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
# market1.current_user.cart.add_item(p, 1)

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