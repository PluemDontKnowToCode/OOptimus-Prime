import sys, os
import Component
main_path = os.path.dirname(__file__) + "\\asset"

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fasthtml.common import *
from backend.lib255 import *

user_id = ""
modal = None

def my_modal(p_id, user_id):
    add_to_cart_modal = Dialog(
                            Div(
                                H3("Pick amount", style = "margin-left: 10px; margin-top: 20px"),
                                    Div(
                                        Form(
                                            Input(
                                                type = "number",
                                                id = "amount",
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
                                style = "border: solid; background-color: #708090; height: 20%; width: 15%;"
                            ),
                            cls = "d1",
                            style = "position: fixed;"
                        ),
    # print(f"Modal from my modal {add_to_cart_modal}")
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
        modal = Dialog(
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
                    cls = "d3",
                    style = "height: 200px; width: 400px;"   
                ),
    # print(f"Modal from validate {modal}")

def view_detail(p_id: int):
    global modal, user_id
    list1 = market1.view_product_detail(p_id)
    p, c = list1
    list_dis = ["Name", "Price", "Stocked", "Description"]
    j1 = create_json(list_dis, p)
    p_image = market1.get_product_image(p_id)
    validate_variable(p_id)
    js_for_dialog = Component.detail_logic()
    login_bool = Component.login_bool
    # print(f"JS {js_for_dialog}\n\n\nand Modal {modal}")
    # print(f"JS \n{js_for_dialog}\n\nMy modal {to_xml(modal)}\n")
    
    part_header = Component.Header()

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
                    cls = "b10" if login_bool else "b11"
                ),
            ),
            stlye = "grid-template-columns: 1fr 1fr;"
        ),
        modal,
        Script(js_for_dialog),
    ),

    # print(f"\n\n\nMy detail {part_detail}")

    part_add_comment = Titled(
        "Add your opinion",
        Form(
            Input(type = "number", id = "star", max = "5", min = "1", value = 3),
            Input(type = "text", id = "new_comment", placeholder = "about your thinking"),
            Button("Submit", type = "submit"),
            method = "post",
            action = f"/add_new_comment/{p_id}"
        )
    ),


    part_comment = Titled("Comment")
    if len(c) > 0:
        part_comment = Titled(
            "Comment",
            Div(*[
                Card(
                    Div(
                        Div(
                            f"{lc["name"]}   {"✯" * lc["star"]}",
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


    page = Main(
        part_header,
        part_detail,
        part_add_comment,   
        part_comment,
        style = Component.configHeader,
    ),
    return page