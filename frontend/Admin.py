from fasthtml.common import *
import Component
import os
import dotenv
from backend.lib255 import *
from datetime import datetime
dotenv.load_dotenv()

def Page():
    requested = market1.current_account.get_requested_product()
    coupon_list = market1.coupon_list
    page = Title("Admin - Teerawee Shop"), Main(
        Component.Header(False, False, "Admin"),
        Grid(
            Div(
                Div(
                    H1(
                        "manage coupon",
                        Style="margin: 2%;"
                    ),
                    A(
                        Button(
                            "Create coupon",
                            
                        ),
                        href="/admin/create_coupon",
                        Style="margin: 2%;"
                    ),
                    
                    Style="""
                        display: flex; 
                        justify-content: space-between;
                        
                    """,
                    id="manage_coupon_head",
                ),
                Div(
                    Div(*
                        [
                            CouponCard(j)
                            for j in coupon_list
                        ],
                        style = "display: flex; ",
                    ),
                    id="manage_coupon_body",
                    style = "height: 20vw;"
                ),
                Style="padding-top:0px;"
            ),
             Div(
                Div(
                    H1(
                        "manage Requested Product",
                        Style="margin: 2%;"
                    ),
                    
                    Style="""
                        display: flex;
                        
                    """,
                    id="manage_requested_head",
                ),
                Div(
                    Div(*
                        [
                            RequestedCard(i)
                            for i in requested
                        ],
                        style = "display: flex; ",
                    ),
                    id="manage_requested_body",
                    style = "height: 20vw;"
                ),
            ),
            Style = """
                grid-template-columns: 1fr;
                grid-template-rows: 1fr 1fr;
                
            """
        ),
        
        Script(Component.get_warn_js() + delete_coupon_pop_up_scirpt),
        Style=Component.configHeader
    )
    
    return page

def delete_coupon_dialog(Coupon):
    return Dialog(
        Div(
            Div(
                f"Are you sure to delete this coupon {Coupon.discount_percent}",
                style = "margin-bottom: 20px;"
            ),
            Div(
                A(
                    Button(
                        "Delete"
                    ),
                    hx_post="/admin/delete_coupon",
                    style = "margin-right: 20px; text-decoration: none; background-color: #eee;"
                ),
                Button(
                    "Cancel",
                    cls = "close_button"
                ),
                style = "blackground-color: white;"
            ),

        ),
        cls = "c_pop_up",
        style = "height: 200px; width: 400px;"   
    ),

delete_coupon_pop_up_scirpt = """
        const openButton = document.querySelectorAll(".open_button")
        const closeButton = document.querySelector(".close_button")
        const modal = document.querySelector(".c_pop_up")
        openButton.forEach(button => button.addEventListener("click", () => modal.showModal()))
        closeButton.addEventListener("click", () => {
            modal.close()
        })\n
    """
def CouponCard(coupon):
    condition = f"Orders ฿{coupon.less_amount}+"
    if(coupon.product_count == 0):
        condition += f" or {coupon.product_count} more products"
    card = Div(
        
        H2(
            f"{coupon.discount_percent}% OFF", 
           Style="margin: 0;"
        ),
        P(
            condition, 
            Style="margin: 0;"
        ),
        Hr(),
        P(
            f"{coupon.start_time} ~ {coupon.end_time}", 
            Style="margin: 0 auto;"
        ),
        Button(
            "X",
            cls = "open_button",
            Style="margin-left: 90%;"
        ),
        delete_coupon_dialog(coupon),
        id=coupon.id,
        Style="border: 1px solid black; padding: 15px; width: 200px; text-align: center; display: inline-block; margin: 10px; position: relative;"
    )
    return card

def RequestedCard(request):
    id = request.product.id
    return Card(
                Div(
                    f"Create By {request.seller.name}"
                ),
                Img(
                    src = f"{request.product.image}",
                    style = "height: 50%; justify-self: center;"),
                Div(
                    f"{request.product.name}"
                ),
                Div(
                    f"{request.product.description}"
                ),
                Div(
                    f"{request.product.price} ฿"
                ),
                Div(
                    Button(
                        "Accept",
                        hx_post=f"/admin/accept/{id}/{True}"
                    ),
                    Button(
                        "Reject",
                        hx_post=f"/admin/accept/{id}/{False}"
                    ),
                    style = "display: flex; flex-direction: row; justify-content: space-between; align-items: center; width:100%;"
                ),
                id = id,
                style = "height: 350px; display: flex; flex-direction: column; justify-content: space-between ; align-items: center; gap:10px; margin: 1%;"
            )

def CreateCouponPage():
    page = Title("Create Coupon - Teerawee Shop"), Main(
        Component.Header(False, False, "Create Coupon"),
        Div(
            Form(  # ฟอร์มข้อมูลสินค้า
                
                Div(Label("Discount Percent:"), Input(type="number", name="discount_percent", min=1, value=1, id="discount_percent"), style="margin-bottom: 20px;"),
                Div(Label("Less Amount:"), Input(type="number", name="less_amount", min=1, value=1, id="less_amount"), style="margin-bottom: 20px;"),
                Div(Label("Product Count:"), Input(type="number", name="product_count", min=1, value=1, id="product_count"), style="margin-bottom: 20px;"),
                Div(Label("Duration:"), Input(type="number", name="duration", min=1, value=1, id="duration"), style="margin-bottom: 20px;"),
                Div(
                    Button("Confirm"),
                    
                    style="margin-top: 20px;"
                ),
                method = "post",
                action = '/admin/create_coupon', 
                id="product_form",
                style="text-align: left; padding: 20px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"
            ),
            style="justify-content: center; align-items: center; height: 100vh; width: 100%;"
        ),


        Style=Component.configHeader + """

        """,
    ),
    return page

def CreateEventPage():
    return