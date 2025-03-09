
class StackItem:
    def __init__(self, product, amount = 1):
        self.__product = product
        self.__amount = self.validate_amount(amount)
        self.__available = True
        
    @property
    def inc_item(self): 
        if self.__amount < self.__product.stock: self.__amount += 1

    @property
    def dec_item(self): 
        if self.__amount >= 0: self.__amount -= 1

    @property
    def product(self): return self.__product

    def validate_amount(self, a1):
        if self.__product.is_greater_than_me(a1):
            return self.__product.stock
        elif a1 <= 0: 
            return None
        else:
            return a1
    
    @property
    def amount(self): return self.__amount
    
    @amount.setter
    def amount(self, a1): self.__amount = self.validate_amount(a1)

    @property
    def to_json(self): return { self.__product: self.__amount }

    def is_me(self, product): return product == self.__product

    @property
    def price(self): return self.__product.price * self.__amount
    
    def update_self(self):
        remain_stock = self.__product.stock
        if self.amount < remain_stock: self.amount = remain_stock