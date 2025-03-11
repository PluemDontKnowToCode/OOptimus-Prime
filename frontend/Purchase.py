from fasthtml.common import *
from backend.lib255 import *
import Component
import frontend._main as _main 

def PurchasePage():
    coupon = market1.current_account.get_coupon()
    cart = market1.get_customer_cart(market1.current_account.id)
    address = market1.current_account.get_address()
    
    pop_up_script = """
        const openButton = document.getElementById("#purchase_button")
        const closeButton = document.getElementById(".b2")
        const modal = document.getElementById(".d1")
        
        openButton.addEventListener("click", () => {{
            modal.showModal()
        }})
        
        closeButton.addEventListener("click", () => {{
            modal.close()
        }})
    """
    popup = Dialog(
                    Div(
                        H3("Are you Sure to purchase", style = "margin-left: 10px; margin-top: 20px"),
                        Div(
                            Div(
                                Button(
                                    "purchase",
                                    type = "submit",
                                    style = "width: 50%; margin-right: 20px;"
                                ),
                                Button(
                                    "close",
                                    id = "b2",
                                ),
                                method = "post",
                                action = f"/purchase/result",
                                style = "margin-left: 10px;"
                            ),
                            Div(
                                
                                style = "position: bottom;"
                            ),
                            
                            style = "display: flex; justify-content: space-betwewen;"
                            
                        ),
                        style = "border: solid; background-color: #708090; height: 20%; width: 15%;"
                    ),
                    id = "d1",
                    style = "position: fixed;"
                ),
    a = None
    district = ""
    province = ""
    zip_code = ""
    phone = ""

    if(market1.current_account.selected_address != None):
        a = market1.current_account.selected_address.to_json()
        district = a['district']
        province = a['province']
        zip_code = a['zip_code']
        phone = a['phone']
    s_coupon = ""
    if(market1.current_account.selected_coupon != None):
        s_coupon = market1.current_account.selected_coupon.id
    page = Title("Cart - Teerawee Shop"), Main(
        Component.Header(),
        Component.TitleHeader("Purchase"),
        Div(
            Div(
                Div(
                    H3("Address",Style="margin-left:6%"),
                    Div(
                        Div(*
                        [
                            AddressCard(i)
                            
                            for i in address
                        ],
                            #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                            id="address",


                            Style="""
                                display: flex; 
                                overflow-x: auto; 
                                scroll-behavior: smooth; 
                                white-space: nowrap; 
                                width: 80%;
                            """
                        ),
                        
                        Style=" display: flex; overflow: hidden; width: 100%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
                Hr(
                    Style="""
                        margin: 0 auto;
                        width:80%;
                        border: 1px solid blue;
                    """
                ),
                Div(
                    Div(
                        H3("Available Coupon"),
                        H4("You can use only one coupon"),
                        Style="margin-left:6%"
                    ),
                    Div(
                        Div(*
                        [
                            CouponCard(i["id"],i["discount_percent"],i["less_amount"],i["start_time"],i["end_time"],product_count=i["product_count"])
                            for i in coupon
                        ],
                            #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                            id="addressSlider",
                            Style="""
                                display: flex; 
                                overflow-x: auto; 
                                scroll-behavior: smooth; 
                                white-space: nowrap; 
                                width: 80%;
                            """
                        ),
                        
                        Style="display: flex; overflow: hidden; width: 100%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
                Style="width: 70%;"
            ),
            Div(
                Div(*
                [
                    Card(
                        Img(
                            src=i['img'],
                            Style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;"),
                        Div(f"{i['name']}(x{i['amount']})"),
                        Div(f"{i['price'] * i['amount']} ฿"),
                        Style="""
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            width: 100%;
                            max-width: 750px;
                            height: 60px;  /* Fixed height */
                            border: ridge;
                            padding: 10px;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                            border-radius: 10px;
                            background-color: white;
                        """,
                        
                    )
                    for i in cart.get_available_product
                    ],
                
                    Style="width:100%;"
                ),
                Div(
                    Hr(Style="border: none; border-top: 3px dashed black; width: 100%;"),
                ),
                Div(
                    Div(
                        H3("SubTotal"),
                        Div(f"{cart.calculate_price()} ฿"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Shipping"),
                        Div(f"50 ฿"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Discount"),
                        Div(f"{get_discount_value() * (cart.calculate_price() + 50)} ฿"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Total"),
                        Div(f"{cart.calculate_price() + 50 - get_discount_value() * cart.calculate_price()} ฿"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    cls="total",
                ),
                Div(
                    Hr(Style="border: none; border-top: 3px dashed black; width: 100%;"),
                ),
                Div(
                    "All Products cannot be returned or exchanged",
                    Style="padding-top: 10px; padding-bottom: 10px;"
                ),
                A(
                    Button("Purchase",
                           Style="width: 100%;",
                           id="purchase_button",
                        ),
                        href=f"/purchase/result/{s_coupon}",
                        Style="padding-top: 10px;"
                ),
                Style="padding-top:0px; width: 25%;"

            ),
            
            Style="display: flex;"
        ),

        #Script(pop_up_script),
        Style="padding: 0px;",
    )
    return page

def ResultPage(result):
    if(result == "success"):
        page = Title("Cart - Teerawee Shop"), Main(
            Component.Header(),
            Component.TitleHeader("Purchase Result"),
            Div(
                H3("Thank you for your purchase"),
                P("Your order has been placed successfully"),
                Button(
                    "Continue Shopping",
                    Style="width: 100%;",
                    hx_get=f"/purchase/redirect/{True}",
                       ),
                Style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 100%;padding-top: 10%;"
            ),
            Style="padding: 0px;",
            
        )
    else:
        page = Title("Cart - Teerawee Shop"), Main(
            Component.Header(),
            Component.TitleHeader("Purchase Result"),
            Div(
                H3("Failed to place order"),
                P(result),
                Button(
                    "Return to Cart",
                    Style="width: 100%;",
                    hx_get=f"/purchase/redirect/{False}",
                    ),
                Style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 100%;"
            ),
            Style="padding: 0px;",
        )
    return page
def AddressCard(a):
    temp = Address(a['district'],a["province"],a["zip_code"],a["phone"])
    if(temp.is_equal(market1.current_account.selected_address)):
        return Card(
                    Div(
                        Div(f"district : {a['district']}",Style="color: #ffffff"),
                        Div(f"province : {a['province']}",Style="color: #ffffff"),
                        Div(f"zip code : {a['zip_code']}",Style="color: #ffffff"),
                        Div(f"phone : {a['phone']}",Style="color: #ffffff"),
                        
                        Style="""
                            width:200px; 
                            margin-left:10px;
                            justify-content: space-between;
                            
                        """,
                        ),
                    Div(
                        Button(
                            "X",
                            hx_post = f"/purchase/apply_address/{a['district']}/{a['province']}/{a['zip_code']}/{a['phone']}",
                            Style="""
                                margin-left:80%;
                                background-color: #ffffff;
                                color: #000000
                            """,
                            )
                    ),
                    Style="background-color: #073763;"
                )
        
    return Card(
                    Div(
                        Div(f"district : {a['district']}"),
                        Div(f"province : {a['province']}"),
                        Div(f"zip code : {a['zip_code']}"),
                        Div(f"phone : {a['phone']}"),
                        
                        Style="""
                            width:200px; 
                            margin-left:10px;
                            justify-content: space-between;
                        """,
                        ),
                    Div(
                        Button(
                            "X",
                            hx_post = f"/purchase/apply_address/{a['district']}/{a['province']}/{a['zip_code']}/{a['phone']}",
                            Style="""margin-left:80%;
                            """
                            )
                    )
                )
def CouponCard(Id,discount, order_min,start_date, end_date,product_count = 0):
    condition = f"Orders ฿{order_min}+"
    if(product_count > 0):
        condition += f" or {product_count} more products"
    card = Div(
        H2(
            f"{discount}% OFF", 
           Style="margin: 0;"
        ),
        P(
            condition, 
            Style="margin: 0;"
        ),
        Hr(),
        P(
            f"{start_date} ~ {end_date}", 
            Style="margin: 0 auto;"
        ),
        SetUpCouponButton(Id),
        
        id=Id,
        Style="border: 1px solid black; padding: 15px; width: 200px; text-align: center; display: inline-block; margin: 10px; position: relative;"
    )
    return card

def get_discount_value():
    if(market1.current_account.selected_coupon != None):
        return market1.current_account.selected_coupon.discount_percent / 100
    return 0

def SetUpCouponButton(Id : str):
    if(market1.current_account.selected_coupon != None):
        if(market1.current_account.selected_coupon.id == Id):
            return Button(
                "USED",
                id=f"button_{Id}",
                Style="margin-top: 10px; padding: 5px 15px; border: 1px solid gray; background: lightgray; color: black;",
                hx_post=f"/purchase/apply_coupon/{Id}",
                hx_swap_oob="true",
    )
    return Button(
            "USE", 
            Style="margin-top: 10px; padding: 5px 15px; border: 1px solid blue; background: white; color: blue;",
            id=f"button_{Id}",
            hx_post=f"/purchase/apply_coupon/{Id}",
            hx_swap_oob="true",
        ),