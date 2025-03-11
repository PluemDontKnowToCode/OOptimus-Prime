from backend.Product import *
from backend.StackItem import *
#region cart
class Cart:
    def __init__(self):
        self.__cart_item_list = []
        self.__unavailable_list = []

    @property
    def size(self):
        res = 0
        for i in self.__cart_item_list:
            res += i.amount
        return res
    
    @property
    def get_cart_item(self): return self.__cart_item_list
    
    @property
    def get_unavailable_item(self): return self.__unavailable_list

    @property
    def product_list(self): return [i.product for i in self.__cart_item_list]
    
    @property
    def get_available_product(self):
        res = []
        # print(len(self.__product_list))
        for i in self.__cart_item_list:
            # print(i, type(i))
            dict1 = i.to_json()
            # print(dict1)
            res.append(dict1)
        # print(res)
        return res
    
    @property
    def get_unavailable_product(self):
        res = []
        # print(len(self.__product_list))
        for i in self.__unavailable_list:
            dict1 = i.to_json()
            # print(dict1)
            res.append(dict1)
        # print(res)
        return res
    
    @property
    def each_stack_amount(self):
        return [i.amount for i in self.__cart_item_list]

    def remove_item(self, product):
        if not isinstance(product, Product): return "Invalid type"
        for i in self.__cart_item_list:
            if i.product.equal(product.id):
                self.__cart_item_list.remove(i)
                return "Remove Complete"
    
        for i in self.__unavailable_list:
            if i.product.equal(product.id):
                self.__unavailable_list.remove(i)
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
                if i.is_me(product): i.amount = amount
                break
        else:
            self.__cart_item_list.append(StackItem(product, amount))
        return "Add Complete"
        
    def calculate_price(self):
        return sum(item.price for item in self.__cart_item_list)
    
    def update_self(self): 
        for i in self.__cart_item_list + self.__unavailable_list: 
            i.update_self()
            
        for i in range(len(self.__cart_item_list)):
            p = self.__cart_item_list[i]
            if not p.available:
                self.__unavailable_list.append(p)
                self.__cart_item_list.pop(i)
                
        for i in range(len(self.__unavailable_list)):
            p = self.__unavailable_list[i]
            if p.available:
                self.__cart_item_list.append(p)
                self.__unavailable_list.pop(i)
        
#endregion