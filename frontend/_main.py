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
import Register
import Comment as com

# h1 = "C://Main//Coding//Python//OOPKMITL//Lab9//OOptimus-Prime"
# sys.path.insert(0, h1)
from backend.lib255 import *

market1.update_current_user(market1.get_account("A000001"))
# print(market1.current_account.name)

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
def get(p_id: str):
    # print(p_id, type(p_id))
    return ItemDetail.view_detail(p_id)

@rt('/add_to_cart/{p_id}/{user_id}')
def post(p_id: str, user_id: str):
    if not market1.current_account: return Redirect('/login')
    res = market1.add_product_to_cart(p_id, user_id)
    print(f"{p_id}, {user_id}, {res}")
    return Redirect(f'/detail/{p_id}')

@rt('/add_new_comment/{p_id}/{star}')
def post(p_id: str, star: int, new_comment: str):
    if not market1.current_account: return Redirect('/login')
    # print(p_id, star, new_comment)
    return com.insert_comment(p_id, star, new_comment)

@rt('/login_process')
def get(name: str, password: str, role: str):
    return Login.validate_login(name, password, role)

@rt('/profile')
def get():
    return Profile.page(market1.current_account)

@rt('/register')
def get():
    return Register.page()

serve(port=3000)