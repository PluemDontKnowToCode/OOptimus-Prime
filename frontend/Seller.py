from fasthtml.common import *
from ItemDetail import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *



def Page():
    my_product = market1.current_account.selling_product
    requested = market1.current_account.get_requested_product()
    page = Title("Seller -Teerawee Shop"), Main(
        Component.Header(False, False, "Seller"),
        Grid(
            Div(
                Div(
                    H1(
                        "My Product",
                        Style="margin: 2%;"
                    ),
                    A(
                        Button(
                            "Add Product",
                            
                        ),
                        href="/addproduct",
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
                            item_post_card(j.image, j.name, j.id, j.price)
                            for j in my_product
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
                            item_post_card(i.image, i.name, i.id, i.price)
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
        style = Component.configHeader
    )
       
    return page
    
def item_post_card(p_img, p_name, p_id, p_price):
    res = Card(
                Img(
                    src = f"{p_img}",
                    style = "height: 50%; justify-self: center;"),
                Div(
                    f"{p_name}"
                ),
                Div(
                    Form(
                        Button(
                            "Detail",
                            type = "submit"
                            ),
                        method = "get",
                        action = f'/detail/{p_id}'
                    ),
                    # Button(
                    #     "Detail",
                    #     hx_get = f'/detail/{p_id}',
                    #     hx_target = "body",
                    #     hx_trigger = "click"
                    # ),
                    Div(
                        f"{p_price} ฿"),
                        style = "display: flex; flex-direction: row; justify-content: space-between; align-items: center; width:100%;"
                    ),
                style = "height: 350px; display: flex; flex-direction: column; justify-content: space-between ; align-items: center; gap:10px;"
            )
    return res



