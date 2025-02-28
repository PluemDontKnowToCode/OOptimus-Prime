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

market = Market()
current_account = None

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
    if(current_account): return CartPage.Page()
    return Redirect('/login')

@rt('/purchase')
def get():
    return Purchase.PurchasePage()

@rt('/purchase/result')
def get():
    result = market.purchase()
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
    return Profile.page(current_account)

serve(port=3000)