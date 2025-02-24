class Market:
    def __init__(self):
        self.__product_list = []
        self.__user = []

    def add_product(self, product1): 
        if isinstance(product1, Product):
            self.__product_list.append(product1)
            return "Done"
        return "Failed"

    def search_product(self, product_id):
        for i in self.__product_list:
            if i.is_this_my_id(product_id): 
                # print("found")
                return i
        return None
    
    def get_product_detail(self, product): return product.detail
    
    def view_product_detail(self, product_id):
        product = self.search_product(product_id)
        return self.get_product_detail(product)
    
    @property
    def product_list(self): return [i for i in self.__product_list]

class Product:
    def __init__(self, name, var_id, price, description, img1):
        self.__name = name
        self.__id = var_id
        self.__price = price
        self.__description = description
        self.__commnet_list = []
        self.__img = img1

    def is_this_my_id(self, var_id): return var_id == self.__id

    def add_comment(self, comment):
        res = ""
        if isinstance(comment, Comment):
            self.__commnet_list.append(comment)
            res = "Done"
        return res

    @property
    def make_detail(self): return [self.__name, self.__id, self.__price, self.__description]

    @property
    def source(self): return self.__img

    @property
    def get_comment_dict(self):
        res = []
        for i in self.__commnet_list:
            res.append(i.convert_to_dict)
        return res
    
    @property
    def get_id(self): return self.__id

    @property
    def detail(self): return [self.make_detail, self.get_comment_dict]
    
    @property
    def name(self): return self.__name

    @property
    def des(self): return self.__description
         

class User:
    def __init__(self, name, market):
        self.__name = name
        self.__market = market

    def view_product_detail(self, product_id): return self.__market.view_product_detail(product_id)

class Comment:
    def __init__(self, name, text, star):
        self.__name = name
        self.__text = text
        self.__star = star
        self.__sym = "✯"
    
    @property
    def convert_to_dict(self):
        return {
            "name": self.__name, 
            "text": self.__text,
            "star": self.__star * self.__sym
        }
    
def create_json(list1, list2):
    res = {}
    for i in range(len(list1)):
        res[list1[i]] = list2[i]
    return res

def set_up():
    m = Market()
    user1 = User("Opor", m)
    p = [Product("Book", 
                 1,
                 200,
                 "Book that everyone can read",
                 "https://cdn-icons-png.flaticon.com/512/8832/8832880.png"),   
         Product("Book more cost",
                 2,
                 250,
                 "Book that rich guy can read",
                 "https://pngimg.com/uploads/book/book_PNG2114.png")
        ]
    c = [Comment("Bruno", "This product is so good", 5)]
    for i in p:
        m.add_product(i)
    p[0].add_comment(c[0])
    return m
