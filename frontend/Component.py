import sys, os
from fasthtml.common import *
main_path = os.path.dirname(__file__) + "\\asset"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.lib255 import *
# file_path = os.path.join(main_path, '/asset')
# print(main_path, file_path)

cartpng = "/cart_removebg_preview.png"
userpng = "/user_imgpng.png"
coupon_basetpng ="/coupon_basket.png"

# print(cartpng)

configHeader = "padding-top: 0px;"
headerfontStyle = """   color: #ffffff
                        """
ButtonHeaderStyle = "margin-right: 10px;"
CheckingStyle = "border: solid;"

login_bool = False

add_to_cart_script = """
        const openButton1 = document.querySelector(".b10")
        const closeButton1 = document.querySelector(".b2")
        const modal1 = document.querySelector(".d1")
        
        openButton1.addEventListener("click", () => {
            modal1.showModal()
        })
        
        closeButton1.addEventListener("click", () => {
            modal.close()
        })\n
    """

alret_scirpt = ""

user_png_script = """
        const openButton2 = document.querySelector(".b3")
        const closeButton2 = document.querySelector(".close_modal2")
        const modal2 = document.querySelector(".user_icon_dialog")
        
        openButton2.addEventListener("click", () => {
            modal2.showModal()
        })
        
        closeButton2.addEventListener("click", () => {
            modal2.close()
        })\n
    """
    
coupon_png_script = """
        const open_coupon_basket_modal = document.querySelector(".coupon_basket")
        const close_coupon_basket_modal = document.querySelector(".close_coupon_basket")
        const modal_coupon_basket = document.querySelector(".coupon_modal")
        
        open_coupon_basket_modal.addEventListener("click", () => {
            modal_coupon_basket.showModal()
        })
        
        close_coupon_basket_modal.addEventListener("click", () => {
            modal_coupon_basket.close()
        })\n
    """
    
user_png_modal = None

warn_to_login_modal = Dialog(
    Div(
        Div(
            "Not login Yet",
            style = "margin-bottom: 20px;"
        ),
        Div(
            A(
                Button(
                    "Go to Login"
                ),
                href = "/login",
                style = "margin-right: 20px; text-decoration: none; background-color: #eee;"
            ),
            Button(
                "Continue as guest",
                cls = "b2"
            ),
            style = "blackground-color: white;"
        ),

    ),
    id = "d2",
    style = "height: 200px; width: 400px;"   
),

def validate_value():
    current_account = market1.current_account
    global alret_scirpt, login_bool
    login_bool = True if current_account else False
    if not login_bool:
        alret_scirpt = """
        const openButton_warn = document.querySelectorAll(".a1")
        const closeButton_warn = document.querySelector(".b2")
        const modal = document.getElementById("d2")
        openButton_warn.forEach(button => button.addEventListener("click", () => modal.showModal()))
        closeButton_warn.addEventListener("click", () => {
            modal.close()
        })\n
    """
    else: alret_scirpt = ""
    alret_scirpt += user_png_script
    
def get_warn_js():
    validate_value()
    return alret_scirpt

def get_home_js():
    validate_value()
    return alret_scirpt + coupon_png_script

def validate_png_modal():
    validate_value()
    global user_png_modal
    mystyle = """
                display: flex;
                flex-direction: column;"""
    mystyle2 = "margin-bottom: 10%;"
    if login_bool:
        user_png_modal = Dialog(
            Div(
                Button(
                    "Logout",
                    onclick = """location.href = "/logout" """,
                    style = mystyle2
                ),
                Button(
                    "View Profile",
                    onclick = """location.href = "/profile" """,
                    style = mystyle2
                ),
                Button(
                    "Close",
                    cls = "close_modal2"
                ),
                style = mystyle
            ),
            cls = "user_icon_dialog",
        ),
    else:
        user_png_modal = Dialog(
            Div(
                Button(
                    "Login",
                    onclick = """location.href = "/login" """,
                    style = mystyle2
                ),
                Button(
                    "Close",
                    cls = "close_modal2"
                ),
                style = mystyle
            ),
            cls = "user_icon_dialog",
        ),

def coupon_card(coupon_dict):
    btn1 = None
    def get_button():
        global login_bool
        
    res = Card(
        H1(coupon_dict['id']),
        Ul(
            Li(f"Discount: {coupon_dict['discount_percent']}%"),
            Li(f"Least Cost: ${coupon_dict['less_amount']}"),
            Li(f"Least Amount: {coupon_dict['product_count']}"),
            Li(f"Date Begin: {coupon_dict['start_time']}"),
            Li(f"Date Expire: {coupon_dict['end_time']}")
        ),
        btn1
    )
    return res

def coupon_modal():
    modal = Dialog(
        Div(
            Div(
                # coupon
                *[coupon_card(i.to_json()) for i in market1.coupon_list],
                style = "flex-direction: column;"  
            ),
            style = ""
        ),
        Button(
                "close",
                cls = "close_coupon_basket",
                style = "margin-left: 1vw;"
        ),
        cls = "coupon_modal"
    )
    return modal
    

def Header(bool_search = True, bool_cart = True, HeaderText = "Teerawee Shop"):
    validate_value()
    validate_png_modal()
    cart_icon = None
    
    part1 = A(
                H1(
                    HeaderText,
                    Style = headerfontStyle
                ), 
                href='/', 
                Style="""
                    text-decoration: none;
                    margin-left: 20px;
                """ + ButtonHeaderStyle
            )
    
    part2 = Div()
    
    if bool_search: part2 = Form(
                    Div(
                        Input(
                            placeholder = "search...",
                            style = "margin: 0px;",
                            id = "search_word"
                            ),
                        style = "width: 25vw;"
                    ),
                    hx_get = "/search_for_home",
                    hx_trigger = "load, keyup delay:250ms",
                    target_id = "grid_home",
                    style = "margin: 0px;"
                )
    
    
    if bool_cart:
        cart_icon = A(
                        Img(
                            src = cartpng,
                            style = "height: 100px;",
                            cls = "a1"
                        ),
                        href = "/cart" if login_bool else "",
                        style = ButtonHeaderStyle
                    )
    
    
    part3 = Div(
                Div(
                    cart_icon,
                    A(
                        Img(
                            src = userpng,
                            style = "height: 70px; z-index: -1;",
                            cls = "b3"
                        ),
                        style = ButtonHeaderStyle
                    ),
                ),
                user_png_modal,
                style = ButtonHeaderStyle + "",
                cls = "user_png1"
                )
    if market1.current_account and isinstance(market1.current_account, Seller): 
        part3 = Div(
                    Div(
                        A(
                            Img(
                                src = userpng,
                                style = "height: 70px; z-index: -1;",
                                cls = "b3"
                            ),
                            style = ButtonHeaderStyle
                        ),
                ),
                user_png_modal,
                style = ButtonHeaderStyle + "",
                cls = "user_png1"
                )
    
    page = Div(
            part1,
            part2,
            part3,
            Style="""
                background-color: #073763; 
                height: 80px; 
                width: 100%; 
                z-index: 1000; 
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); 
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
                """,
        )
    
    return page

def TitleHeader(text):
    return H1(
        text, 
        Style="""padding-top: 30px; 
        margin-left: 15%; 
        display: flex;"""
              ),

