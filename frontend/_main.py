from fasthtml.common import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

from dotenv import load_dotenv
load_dotenv()

import Component
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
    return Profile.page()

@app.get('/register')
def register():
    return Register.page()

@app.get('/cart')
def cart():
    if(market1.current_account != None): return CartPage.Page()
    return Redirect('/login')

@app.get('/purchase')
def purchase():
    try:

        if(market1.current_account.cart != None and market1.current_account.cart.size > 0):
            return Purchase.PurchasePage()
        return Redirect('/cart')
    except:
        return Redirect("/")

@app.get('/purchase/result/{address}/{coupon}')
def purchhase_result():
    result = market1.purchase()
    return Purchase.ResultPage(result)

@app.get('/detail/{p_id}')
def detail(p_id: str):
    return ItemDetail.view_detail(p_id)

@app.post('/add_to_cart/{p_id}/{user_id}')
def add_to_cart(p_id: str, user_id: str, amount: int):
    # print("route", amount)
    if not market1.current_account: return Redirect('/login')
    res = market1.add_product_to_cart(p_id, user_id, amount)
    return Redirect(f'/detail/{p_id}')

@app.post('/add_new_comment/{p_id}')
def add_new_commnet(p_id: str, star: int, new_comment: str):
    if not market1.current_account: return Redirect('/login')
    return com.insert_comment(p_id, star, new_comment) 

#delete card code
@app.delete("/cart/remove/{id}")
async def Remove(id : str):
    print(id + " : Click!!"), 
    market1.current_account.cart.remove_item(market1.get_product(id))
    
    userCart = market1.get_customer_cart_product(market1.current_account)
    price = 0
    if (userCart): 
        for i in userCart:
            price += i.price

    return Redirect('/cart')
    # return Div(
    #     Div("",id=id, hx_swap="outerHTML"),
    #     Button(f"Check Out ({len(userCart)})", id="lenCart", hx_swap_oob="true"),
    #     Div(f"Total: {price}", id="price", hx_swap_oob="true"),
    #     UpdateCartUI()
    # ),

@app.post("/cart/add")
async def Add():
    p = market1.get_product("P000001")
    # print(p)
    market1.current_account.cart.add_item(p)

@app.post("/apply_coupon/{id}")
async def apply_coupon(id: str):
    global selected_coupon
    # Save selected coupon (assuming it's stored in market1.current_account)
    selected_coupon = market1.current_account.get_coupon(id)
    
    return Button(
        "USED",
        id="button_{Id}",
        Style="margin-top: 10px; padding: 5px 15px; border: 1px solid gray; background: lightgray; color: black;",
        hx_swap_oob="true",
    )

serve(port=3000)