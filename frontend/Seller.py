from fasthtml.common import *
from ItemDetail import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *



# print(all_product)
# for p in all_product:
#     print(f"ID: {p.id}")

def Page():
    all_UnImproveProduct = market1.requested_list
    head = Component.Header(False)
    body = Grid(
        Grid(
            *[Card(
                Img(
                    src = f"{i.product.image}",
                    style = "height: 50%; justify-self: center;"),
                Div(
                    f"{i.product.name}"
                ),
                Div(
                    Form(
                        Button(
                            "Detail",
                            type = "submit"
                            ),
                        method = "get",
                        action = f'/detail/{i.product.id}'
                    ),
                    Div(
                        f"{i.product.price} ฿"),
                        style = "display: flex; flex-direction: row; justify-content: space-between; align-items: center; width:100%;"
                    ),
                style = Component.CheckingStyle + "height: 350px; display: flex; flex-direction: column; justify-content: space-between ; align-items: center; gap:10px;"
            ) for i in all_UnImproveProduct],
            style = "grid-template-columns: 1fr ;"
        ),
        style = "grid-template-columns: 25% 70%"
    )
    page = Main(
        head,
        body,
        Component.warn_to_login_modal,
        Script(Component.get_warn_js()),
        style = Component.configHeader
    )
    return page
    