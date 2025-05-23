from backend.Account import *
from backend.Coupon import *
from backend.Transaction import *
from backend.Category import *

class Customer(Account):
    def __init__(self, id= '', name = "", username = "", password ="", money = 10000 ,address = [],image = "user_imgpng.png",coupon = [],market = None):
        super().__init__(id, name,username, password, money,address, image, market)
        self.__cart = Cart()
        self.__transaction = []
        self.__coupon_list = coupon
        self.__selected_coupon = None
        self.__selected_address= None
    
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
    def selected_coupon(self):
        return self.__selected_coupon
    
    @property
    def selected_address(self):
        return self.__selected_address

    
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
    
    def delete_coupon(self, coupon : Coupon):
        for i in self.__coupon_list:
            if i.equal(coupon.id):
                self.__coupon_list.remove(i)
                return "Remove Complete"
        return "Not Found"
    
    def is_have_coupon(self, coupon_id):
        for i in self.__coupon_list:
            if i.equal(coupon_id): return True
        return False
    
    def update_selected_coupon(self, coupon):
        self.__selected_coupon = coupon
        return "Update Coupon Complete"
    
    def update_selected_address(self, address):
        self.__selected_address = address
        return "Update Address Complete"

   
    def add_to_cart(self, product : Product, amount):
        return self.__cart.add_item(product, amount)
        
    def clear_cart(self):
        self.__cart.clear()

    def add_transaction(self, transaction1):
        if isinstance(transaction1, Transaction): self.__transaction.append(transaction1)
        return
    
    def update_money(self, amount):
        super().update_money(amount)
        return
    
    def view_product_detail(self, product_id): return self.__market.view_product_detail(product_id)

    def get_transaction_list(self):
        return self.__transaction

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
    def add_address(self, district, province, zip_code, phone_number):
        for address in super().address_list:
                if address.district == district and address.province == province and address.zip_code == zip_code and address.phone_number == phone_number:
                    return 'Address already exists.'
            
        new_address = Address(district=district, province=province, zip_code=zip_code, phone_number=phone_number)
        super().address_list.append(new_address)
        return 'success'