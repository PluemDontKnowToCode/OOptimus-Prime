from fasthtml.common import *
from Component import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

from dotenv import load_dotenv
load_dotenv()

market = Market()

import Admin
import Home
import Seller
import Cart
import Login
import ItemDetail
import Purchase

app,rt = fast_app(
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
    return Cart.CartPage()

@rt('/purchase')
def get():
    return Purchase.PurchasePage()

@rt('/lobby')
def get():
    return ItemDetail.slots

@rt('/detail/{p_id}')
def get(p_id):
    return ItemDetail.view_detail(p_id)

serve()