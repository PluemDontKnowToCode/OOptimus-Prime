import sys, os
import Component
main_path = os.path.dirname(__file__) + "\\asset"

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fasthtml.common import *
from backend.lib255 import *

user_id = ""
modal = None

def my_modal(p_id, user_id):
    p = market1.get_product(p_id)
    if not p: p = market1.get_requested(p_id)
    p_stock = p.stock
    add_to_cart_modal = Dialog(
        Div(
            H3("Pick amount", style = "margin-left: 10px; margin-top: 20px"), H3(f"Aavaiable: {p_stock}", style = "margin-left: 10px; margin-top: 20px"),
                Div(
                    Form(
                        Input(
                            type = "number",
                            id = "amount",
                            min = "1",
                            max = f"{p_stock}",
                            value = "1",
                            style = "width: 70%;"
                        ),
                        Button(
                            "push product",
                            type = "submit",
                            style = "width: 50%; margin-right: 20px;"
                        ),
                        Button(
                            "close",
                            cls = "b2",
                        ),
                        method = "post",
                        action = f"/add_to_cart/{p_id}/{user_id}",
                        style = "margin-left: 10px;"
                    ),
                    style = "display: flex; justify-content: space-betwewen;"
                
            ),
            style = "border: solid; background-color: #708090; height: 25vw; width: 20vw;"
        ),
        cls = "d1"
    ),
    return add_to_cart_modal



def validate_variable(p_id):
    acc = market1.current_account
    global user_id, modal
    if acc:
        user_id = acc.id
        modal = my_modal(p_id, user_id)
    else:
        # print("NO ACCOUNT")
        user_id = "NONE"
        modal = Component.warn_to_login_modal
        
        
        

def view_detail(p_id: int):
    global modal, user_id
    list1 = market1.view_product_detail(p_id)
    p, c = list1
    list_dis = ["Name", "Price", "Stocked", "Description"]
    j1 = create_json(list_dis, p)
    p_image = market1.get_product_image(p_id)
    approve_bool = market1.is_product_approve(p_id)
    login_bool = Component.login_bool
    js_for_dialog = Component.get_warn_js()
    if login_bool: js_for_dialog += ("\n" + Component.add_to_cart_script)
    validate_variable(p_id)
    role = None
    if isinstance(market1.current_account, Customer): role = "customer"
    if isinstance(market1.current_account, Seller): role = "seller"
    if isinstance(market1.current_account, Admin): role = "admin"
    
    part_header = Component.Header(False, True if role == "customer" else False)

    part_detail = Titled(
        "Detail",
        Grid(
            Img(
                 src = f"/{p_image}",
                 style = "height: 70%; justify-self: center;"
                ),
            Div(
                *[Card(
                    Div(
                        f"{i}: {j}"
                    )
                ) for i, j in j1.items()],
                Button(
                    "Add to cart",
                    cls = "b10" if login_bool else "a1",
                ) if (j1['Stocked'] > 0 and role == "customer") else Div(),
                modal,
            ),
            stlye = "grid-template-columns: 1fr 1fr;"
        ),
    ),

    part_add_comment = Div()
    if (login_bool and role == "customer"): part_add_comment = Titled(
        "Add your opinion",
        Form(
            Div(Input(type = "number", id = "star", max = "5", min = "1", value = 3), style = "width: 5%;"),
            Div(Input(type = "text", id = "new_comment", placeholder = "about your thinking", style = "height: 6vw;"), style = "width: 50%;"),
            Div(Button("Submit", type = "submit"), style = "width: 10vw;"),
            method = "post",
            action = f"/add_new_comment/{p_id}" if login_bool else ""
        )
    ),
    
    
    part_comment = Titled("Comment")
    if len(c) > 0 and (role != "admin"):
        part_comment = Titled(
            "Comment",
            Div(*[
                Card(
                    Div(
                        Div(
                            f"{lc['name']}   {'✯' * lc['star']}",
                            Card(
                                lc["text"], style = ""
                            )
                        )
                    ),
                    Style = "width: 50%; margin-right: 2%; "
                ) 
                for lc in c],
            Style="""
                    display: flex; 
                    flex-direction: column;
                    overflow-x: auto; 
                    scroll-behavior: smooth; 
                    white-space: nowrap; 
                    width: 100%;
                """
        ),
    ),
        
    if not approve_bool: part_comment = Div()

    page = Main(
        part_header,
        part_detail,
        part_add_comment,   
        part_comment,
        modal,
        Script(js_for_dialog),
        style = Component.configHeader,
    ),
    return page