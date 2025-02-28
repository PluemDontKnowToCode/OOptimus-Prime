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

# h1 = "C://Main//Coding//Python//OOPKMITL//Lab9//OOptimus-Prime"
# sys.path.insert(0, h1)
from backend.lib255 import *

market = Market()

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
    return CartPage.Page()

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

serve(port=3000)