import sys, os
import Component
main_path = os.path.dirname(__file__) + "\\asset"

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fasthtml.common import *
from backend.lib255 import *

def view_detail(p_id: int):
    # print(f"ID: {p_id}, Type: {type(p_id)}")
    list1 = market1.view_product_detail(p_id)
    p, c = list1
    list_dis =["Name", "Price", "Stocked", "Description"]
    j1 = create_json(list_dis, p)
    p_image = market1.get_product_image(p_id)
    user_id = market1.current_account.id if market1.current_account else 'NONE'
    # print(j1)
    part_header = Component.Header()
    
    js_for_dialog = Component.add_to_cart_script
    
    buttonSize = "height: 10%; width: 25%;"

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
                    cls = "b1"
                ),
                Dialog(
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
                Script(js_for_dialog)
            ),
            stlye = "grid-template-columns: 1fr 1fr;"
        ),
        # Div(
        #     "data-overlay",
        #     cls = "overlay"
        # ),
        # Div(
        #     "data-modal",
        # )
    )


    part_add_comment = Titled(
        "Add your opinion",
        Form(
            Input(type = "number", id = "star", max = "5", min = "1", value = 3),
            Input(type = "text", id = "new_comment", placeholder = "about your thinking"),
            Button("Submit", type = "submit"),
            method = "post",
            action = f"/add_new_comment/{p_id}"
        )
    )


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
    )


    page = Main(
        part_header,
        part_detail,
        part_add_comment,   
        part_comment,
        style = Component.configHeader
    )
    return page

# def slots():
#     plist = market01.product_list
#     page = Titled("Teerawee's Shop",
#        Div(*[Card(
#             Div(
#                 Div(
#                     H3(p.name), 
#                     P(p.description)), 
#                 Div(
#                     Form(
#                         Button("view detail", type = "summit"),
#                         method = "get",
#                         action = f"/detail/{p.id}"
#                         )    
#                     ),
#                     Style = "display: block; justify-content: space-between;"), 
#             Img(src = p.image, Style = "width: 25%; height: auto;"), 
#             Style = "display: flex; justify-content: space-between;") for p in plist]))
#     # for i in plist:
#     #     print(i.get_id)
#     return page

# @rt("/add_comment/{user_name}/{text}/{star}/{p_id}")
# def post(user_name, text, star, p_id):
#     com1 = Comment(user_name, text, star)
#     market01.add_comment_to_product(p_id, com1)