from fasthtml.common import *
from Component import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

from dotenv import load_dotenv
load_dotenv()

import Admin
import Home
import Seller
import CartPage
import Login
import ItemDetail
import Purchase
import Profile

# h1 = "C://Main//Coding//Python//OOPKMITL//Lab9//OOptimus-Prime"
# sys.path.insert(0, h1)
from backend.lib255 import *

market1.update_current_user(market1.get_account("A000001"))
print(market1.current_account.name)






main_path = os.path.dirname(__file__) + "\\asset"
# print(main_path)

app,rt = fast_app(
    static_path = main_path,
    hdrs=[Style(':root { --pico-font-size: 100%; }')],
    id=int, title=str, done=bool, pk='id')

@rt('/')
def get():
    return Home.Page()

@rt('/login')
def get():
    return Login.Page()

@rt('/cart')
def get():
    if(market1.current_account): return CartPage.Page()
    return Redirect('/login')

@rt('/purchase')
def get():
    if(len(market1.current_account.cart.product_list) > 0):
        return Purchase.PurchasePage()
    return Redirect('/cart')

@rt('/purchase/result')
def get():
    result = market1.purchase()
    return Purchase.ResultPage(result)

@rt('/detail/{p_id}')
def get(p_id: int):
    # print(p_id, type(p_id))
    return ItemDetail.view_detail(p_id)

@rt('/login_process')
def get(name: str, password: str):
    # print(name, password)
    current_account = market1.verify_user(name, password)
    # print(current_account)
    if(current_account): return Redirect('/')
    return Redirect('/login')

@rt('/profile')
def get():
    return Profile.page(market1.current_account)

serve(port=3000)