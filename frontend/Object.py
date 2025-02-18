class Object:
    def __init__(self, id):
        self.__id = id


class Product(Object):
    def __init__(self, id):
        super().__init__(id)

class Customer(Object):
    def __init__(self, id,money = 0):
        super.__init__(id)
        self.__money = money
        self.__cart = Cart()
        self.__transaction = []

    @property
    def cart(self):
        return self.__cart
    
    def add_transaction(self):
        return
    
    def update_money(self, amount):
        self.__money += amount
        return
    
    def cart_product(self):
        return self.__cart.product_list
    
class Transaction():
    def __init__(self, customer_id, product_id):
        pass
    
    
class Market():
    def __init__(self):
        self.__user_list = []
        self.__product_list = []
        

    def purchase(self, user_id, address, coupon, money):
        pass

    def get_product(self, id):
        return
    
    def get_user(self, id):
        return

class Cart:
    def __init__(self):
        self.__product_List = []

    def remove_product(self, product_id):
        return

    @property
    def product_list(self):
        return self.__product_List