from datetime import *
import backend.StackItem
import backend.Product

#region Transaction
class Transaction:
    def __init__(self, product_list, amount_list):
        self.__data = self.make_data(product_list, amount_list)
        self.__net_price = self.sum_of_me(product_list, amount_list)
        self.__date = datetime.now()

    @property
    def date(self):
        return self.__date
    
    @property
    def data(self):
        return self.__data
    
    @property
    def net_price(self):
        return self.__net_price

    
    def make_data(self, product_list, amount_list):
        res = []
        for i in range(len(product_list)):
            temp_str = f"{product_list[i].name}, {product_list[i].price}฿ x {amount_list[i]} =  {product_list[i].price * amount_list[i]}฿"
            res.append(temp_str)
        return res
    
    def sum_of_me(self, product_list, amount_list):
        res = 0
        for i in range(len(product_list)): res += (product_list[i].price * amount_list[i])
        return res
    
#endregion