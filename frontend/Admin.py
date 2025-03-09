from fasthtml.common import *
import Component
import os
import dotenv
from backend.lib255 import *
from datetime import datetime
dotenv.load_dotenv()

requestMock = [
    [market1.get_account("S000001"), market1.product_list[0], datetime.now()],
    [market1.get_account("S000001"), market1.product_list[1], datetime.now()],
]
def Page():
    requested = market1.current_account.get_requested_product()
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
                    id="manage_coupon_body",
                    style = "height: 20vw;"
                ),
                Style="padding-top:0px;"
            ),
            Div(
                Div(
                    H1(
                        "manage event",
                        Style="margin: 2%;"
                    ),
                    Div(
                        Button(
                            "Create event",
                            href="/admin/createEvent"
                        ),
                        Style="margin: 2%;"
                    ),
                    
                    Style="""
                        display: flex; 
                        justify-content: space-between;
                        
                    """,
                    id="manage_event_head",
                ),
                Div(
                    id="manage_event_body",
                    style = "height: 20vw;"
                ),
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
                            manageRequestedCard(i)
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
        Script(Component.get_warn_js()),
        Style=Component.configHeader
    )
    
    return page


def manageCouponCard():

    return 

def manageEventcard():
    return

def manageRequestedCard(request):
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
                Div(Label("Product Name:"), Input(type="text", name="name", id="product_name"), style="margin-bottom: 20px;"),
                Div(Label("Description:"), Textarea(name="description", rows=3, id="description"), style="margin-bottom: 20px;"),
                Div(Label("Price (฿):"), Input(type="number", name="price", step="0.01", id="price"), style="margin-bottom: 20px;"),
                Div(Label("Quantity:"), Input(type="number", name="quantity", min=1, value=1, id="quantity"), style="margin-bottom: 20px;"),
                Div(Label("Category (use only English):"), Input(type="text", name="category", id="category"), style="margin-bottom: 20px;"),
                Div(Label("Image URL:"), Input(type="text", name="image_url", id="image_url"), style="margin-bottom: 20px;"),
                Div(Button("Confirm", type="button", onclick="submitForm()"), style="margin-top: 20px;"),
                method="post",
                action="/add_coupon",
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