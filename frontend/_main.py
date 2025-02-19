from fasthtml.common import *
import os

from dotenv import load_dotenv
load_dotenv()

import Admin
import Home
import Seller
import Cart
import Login

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
    return Cart.Page()

serve()