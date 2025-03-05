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

start = fast_app(
    static_path = main_path,
    hdrs=[Style(':root { --pico-font-size: 100%; }')],
    id=int, title=str, done=bool, pk='id')

app = start[0]

@app.get('/')
def root():
    return Home.Page()

@app.get('/login')
def login():
    return Login.Page()

@app.get('/login_process')
def login_process(name: str, password: str, role: str):
    return Login.validate_login(name, password, role)

@app.get('/profile')
def profile():
    return Profile.page(market1.current_account)

@app.get('/register')
def register():
    return Register.page()

@app.get('/cart')
def cart():
    if(market1.current_account): return CartPage.Page()
    return Redirect('/login')

@app.get('/purchase')
def purchase():
    if(len(market1.current_account.cart.product_list) > 0):
        return Purchase.PurchasePage()
    return Redirect('/cart')

@app.get('/purchase/result')
def purchhase_result():
    result = market1.purchase()
    return Purchase.ResultPage(result)

@app.get('/detail/{p_id}')
def detail(p_id: str):
    return ItemDetail.view_detail(p_id)

@app.post('/add_to_cart/{p_id}/{user_id}')
def add_to_cart(p_id: str, user_id: str):
    if not market1.current_account: return Redirect('/login')
    res = market1.add_product_to_cart(p_id, user_id)
    return Redirect(f'/detail/{p_id}')

@app.post('/add_new_comment/{p_id}/{star}')
def add_new_commnet(p_id: str, star: int, new_comment: str):
    if not market1.current_account: return Redirect('/login')
    return com.insert_comment(p_id, star, new_comment)

serve(port=3000)