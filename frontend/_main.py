from fasthtml.common import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

from dotenv import load_dotenv
load_dotenv()

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse, FileResponse
import os
import base64
import Component
import Admin as admin
import Home
import Seller as sel
import CartPage
import Login
import ItemDetail
import Purchase
import Profile
import Register
import Addproduct
import Transactionz
import AddressPage

import Comment as com
import Addproduct as addp

# h1 = "C://Main//Coding//Python//OOPKMITL//Lab9//OOptimus-Prime"
# sys.path.insert(0, h1)
from backend.lib255 import *

# print(market1.current_user.name)



main_path = os.path.dirname(__file__) + "\\asset"
# print(main_path)

start = fast_app(
    static_path = main_path,
    hdrs=[Style(':root { --pico-font-size: 100%; }')],
    id=int, title=str, done=bool, pk='id')

app = start[0]

#region Main and User
@app.get('/')
def root():
    if market1.current_user and isinstance(market1.current_user, Seller): 
        return sel.Page()
    if market1.current_user and isinstance(market1.current_user ,Admin): 
        return admin.Page()
    return Home.Page()

@app.get('/addproduct')
def addproduct():
    return Addproduct.Page()

@app.post('/addrequestproduct')
def addproduct(name: str, description: str, price: str, quantity: str, category: str, image_url: str):
    if isinstance(market1.current_user, Seller): 
        return addp.insert_request(name, description, price, quantity, category, image_url)
    return Redirect('/login')
    

@app.get('/login')
def login():
    return Login.Page()

@app.get('/login_process')
def login_process(name: str, password: str, role: str):
    return market1.validate_login(name, password, role)

@app.get('/logout')
def logout():
    market1.update_current_user(None)
    return Redirect('/')

@app.get('/register')
def register():
    return Register.page()

@app.post('/register')
async def registor(name : str, password : str, r_password : str, role : str):
    result = Register.validate_register(name, password, r_password, role)
    if(result == 'success'):
        return Redirect("/")
    return Redirect("/register")

@app.get('/profile')
def profile():
    return Profile.page()

@app.post('/profile/change_name')
def profile_change_name(new_username: str):
    market1.change_username(new_username)
    return Redirect('/profile')

@app.post('/profile/update_image')
async def update_profile_image(request: Request):
    form = await request.form()
    base64_str = form.get('file')
    filename = form.get('filename')
    
    if not base64_str or not filename:
        return JSONResponse({'success': False, 'message': 'No file uploaded.'})
    
    file_location = f"static/profile_images/{filename}"
    try:
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as f:
            f.write(base64.b64decode(base64_str))
        
        image_url = f"/profile_images/{filename}"
        market1.update_user_image(image_url)
        return JSONResponse({'success': True, 'image_url': image_url})
    
    except Exception as e:
        return JSONResponse({'success': False, 'message': str(e)})

@app.get('/profile_images/{filename}')
async def get_profile_image(filename: str):
    file_path = f"static/profile_images/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return JSONResponse({'success': False, 'message': 'File not found'})


@app.get('/address')
def address():
    return AddressPage.page()

@app.post('/address/add')
def add_address(district: str, province: str, zip_code: str, phone_number: str):
    market1.add_user_address(district, province, zip_code, phone_number)
    return Redirect('/address')

@app.post('/address/delete')
async def delete_address(request: Request):
    data = await request.json()
    district = data.get('district')
    market1.delete_address(district)
    return JSONResponse({'success': True})



@app.get('/transaction')
def transaction():
    return Transactionz.Page()

#end

#region Search
@app.get('/search_for_home')
def searching1(search_word: str):
    return Home.get_item_post_card(search_word)

# @app.get('/search_for_cart')
# def searching2(search_word: str):
#     pass

@app.get('/search_for_seller')
def searching2(search_word: str):
    pass


@app.get('/category/{name}')
async def search_by_category(name : str):
    current = market1.get_category(name)
    return Home.get_item_post_card_by_list(market1.search_by_category(current))
#end

#region Item's Detail
@app.get('/detail/{p_id}')
def detail(p_id: str):
    return ItemDetail.view_detail(p_id)

@app.post('/add_new_comment/{p_id}')
def add_new_commnet(p_id: str, star: int, new_comment: str):
    if not market1.current_user: return Redirect('/login')
    return com.insert_comment(p_id, star, new_comment) 

#end

#region Cart and Payment
@app.get('/cart')
def cart():
    if(market1.current_user): return CartPage.Page()

@app.get('/purchase')
def purchase():
        if(market1.current_user.cart != None and market1.current_user.cart.size > 0):
            return Purchase.PurchasePage()
        return Redirect('/cart')

@app.get('/purchase/result/{coupon_id}')
def purchase_result(coupon_id : str):
    coupon = market1.get_coupon(coupon_id)
    result = market1.purchase(market1.current_user.id, coupon)
    return Purchase.ResultPage(result)

@app.post('/add_to_cart/{p_id}/{user_id}')
def add_to_cart(p_id: str, user_id: str, amount: int):
    if not market1.current_user: return Redirect('/login')
    res = market1.add_product_to_cart(p_id, user_id, amount)
    return Redirect(f'/detail/{p_id}')

#delete card code
@app.delete("/cart/remove/{id}")
async def Remove(id : str):
    market1.current_user.cart.remove_item(market1.get_product(id))
    return Redirect('/cart')

@app.get("/purchase/redirect/{success}")
async def PurchaseRedirect(success : bool):
    if(success):
        return Redirect("/")
    return Redirect("/cart")

@app.post("/cart/add")
async def Add():
    p = market1.get_product("P000001")
    # print(p)
    market1.current_user.cart.add_item(p)

@app.post("/purchase/apply_coupon/{id}")
async def apply_coupon(id: str):
    # print("Coupon : " + id)
    # Save selected coupon (assuming it's stored in market1.current_user)
    if(market1.current_user.selected_coupon == None or id != market1.current_user.selected_coupon.id):
        select = market1.get_coupon(id)
        if(select.check_condition(market1.current_user.cart)):
            market1.current_user.update_selected_coupon(market1.get_coupon(id))
    else:
        market1.current_user.update_selected_coupon(None)
    return Redirect("/purchase")

@app.post("/purchase/apply_address/{district}/{province}/{zip_code}/{phone_number}")
async def apply_address(district : str, province : str, zip_code : str, phone_number : str):
    address = Address(district, province, zip_code, phone_number)
    for a in market1.current_user.address_list:
        if(a.is_equal(address)):
            market1.current_user.update_selected_address(address)
    return Redirect("/purchase")

#end

#region Admin and Coupon
@app.get("/admin/create_coupon")
def create_coupon_page():
    if market1.current_user and isinstance(market1.current_user ,Admin): 
        return admin.CreateCouponPage()
    return Redirect("/")

@app.post("/admin/create_coupon")
async def add_coupon(discount_percent : int,less_amount : float, product_count : int, duration : int):
    if market1.current_user and isinstance(market1.current_user ,Admin): 
        market1.current_user.create_coupon(discount_percent, less_amount, product_count, duration)
    return Redirect("/")

@app.post("/admin/delete_coupon/{id}")
async def delete_coupon(id : str):
    print(id)
    if market1.current_user and isinstance(market1.current_user ,Admin): 
        print(market1.current_user.delete_coupon(id))
    return Redirect("/")

@app.post("/admin/accept/{id}/{status}")
async def accept_request(id : str, status : bool):
    if isinstance(market1.current_user, Admin):
        if(status):
            market1.current_user.approve_product(market1.get_requested(id))
        else:
            market1.current_user.reject_product(market1.get_requested(id))

    return Redirect("/")

@app.get("/customer/add_coupon/{coupon_id}")
def add_coupon_to_account(coupon_id: str):
    if market1.current_user and isinstance(market1.current_user, Customer):
        market1.add_coupon_to_current_user(coupon_id)
    return Div()

#end
serve(port=3000)

