from backend.Product import *
from backend.StackItem import *
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
        # print(len(self.__product_list))
        for i in self.__cart_item_list:
            dict1 = i.product.to_json()
            dict1.update({"amount": i.amount})
            # print(dict1)
            res.append(dict1)
        # print(res)
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
        return sum(item.price for item in self.__cart_item_list)
        
#endregion