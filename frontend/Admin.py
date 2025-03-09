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
                    Div(
                        Button(
                            "Create coupon",
                            hx_get="/admin/createCoupon"
                        ),
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
                            hx_get="/admin/createEvent"
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
    return

def CreateEventPage():
    return