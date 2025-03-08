from fasthtml.common import *
from ItemDetail import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

all_product = get_all_product()

# print(all_product)
# for p in all_product:
#     print(f"ID: {p.id}")
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

def Page(prodcut_pool = [], search_word = ""):
    result = None
    if len(prodcut_pool) == 0 and search_word == "": result = [item_post_card(i.image, i.name, i.id, i.price) for i in all_product]
    else: result = [item_post_card(i['img'], i['name'], i['id'], i['price']) for i in prodcut_pool]
    head = Component.Header()
    body = Grid(
        Div(
            Div(
                "Category",
                style = "text-align: center;"
            ),
            style = Component.CheckingStyle
        ),
        Div(
            
        ),
        Div(
            # *result,
            style = "grid-template-columns: 1fr 1fr 1fr 1fr;",
            id = "grid_home"
        ),
        style = "grid-template-columns: 10% 1.1% 70%"
    )
    page = Main(
        head,
        body,
        Component.warn_to_login_modal,
        Script(Component.get_warn_js()),
        style = Component.configHeader
    )
    return page
    