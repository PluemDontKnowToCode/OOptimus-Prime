from fasthtml.common import *
from Component import *
import os
import sys
from Object import *
from dotenv import load_dotenv
load_dotenv()

import Admin
import Home
import Seller
import Cart
import Login

h1 = "C://Main//Coding//Python//OOPKMITL//Lab9//OOptimus-Prime"
sys.path.insert(0, h1)
from backend.lib255 import *

market = Market()

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
    return Cart.PurchasePage()

serve()
