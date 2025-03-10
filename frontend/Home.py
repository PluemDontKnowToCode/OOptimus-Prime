from fasthtml.common import *
from ItemDetail import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

all_product = get_all_product()

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

def get_item_post_card(search_word):
    list1 = market1.search(search_word)
    # print(search_word)
    # print(f"res: {list1}")
    if not list1: return None
    return Grid(*[item_post_card(i['img'], i['name'], i['id'], i['price']) for i in list1], style = "grid-template-columns: 1fr 1fr 1fr 1fr;")

def get_item_post_card_by_list(list_temp):
    list1 = list_temp
    # print(search_word)
    # print(f"res: {list1}")
    if not list1: return None
    return Grid(*[item_post_card(i['img'], i['name'], i['id'], i['price']) for i in list1], style = "grid-template-columns: 1fr 1fr 1fr 1fr;")

def Category_button(i):
    

    return Div(
            Button(
                i.name,
                Style="""
                    color:black;
                    background:white;
                    background-color: white;
                    border: 1px solid black;
                    padding: 10px 15px;
                    text-align: left;
                    font-size: 16px;
                    cursor: pointer;
                    width: 100%;
                """,
                
            ),
            hx_get=f"/category/{i.name}",
            target_id="grid_home",
            hx_trigger="click",
            id="i.name"
        )

def Page():
    head = Component.Header()
    body = Grid(
        Div(
            Div(
                "Category",
                style = "text-align: center;"
            ),
            Div(*
                
                [
                    Category_button(i)
                    for i in market1.category_list
                ],
                style="""
                    display:flex;
                    flex-direction: column;
                """
            ),
            
            style = Component.CheckingStyle,
        ),
        Div(
            
        ),
        Div(
            # *result,
            style = "grid-template-columns: 1fr 1fr 1fr 1fr;",
            id = "grid_home"
        ),
        Div(
            # coupon
            Img(
                src = Component.coupon_basetpng,
                cls = "coupon_basket" if Component.login_bool else "a1"
            ),
            Component.coupon_modal()
            # style = "border: solid;",
        ),
        style = "grid-template-columns: 10% 1.1% 70% 10%"
    )
    page = Main(
        head,
        body,
        Component.warn_to_login_modal,
        Script(Component.get_warn_js()),
        style = Component.configHeader
    )
    return page
    