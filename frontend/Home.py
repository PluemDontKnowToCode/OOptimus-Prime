from fasthtml.common import *
from ItemDetail import *
from Component import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

all_product = get_all_product()

# print(all_product)
# for p in all_product:
#     print(f"ID: {p.id}")

def Page():
    head = Header()
    body = Grid(
        Div(
            Div(
                "Category",
                style = "text-align: center;"
            ),
            style = CheckingStyle
        ),
        Grid(
            *[Card(
                Img(
                    src = f"{i.image}",
                    style = "height: 50%; justify-self: center;"),
                Div(
                    f"{i.name}"
                ),
                Div(
                    Form(
                        Button(
                            "Detail",
                            type = "submit"
                            ),
                        method = "get",
                        action = f'/detail/{i.id}'
                    ),
                    Div(
                        f"{i.price} ฿"),
                        style = "display: flex; flex-direction: row; justify-content: space-between; align-items: center; width:100%;"
                    ),
                style = CheckingStyle + "height: 350px; display: flex; flex-direction: column; justify-content: space-between ; align-items: center; gap:10px;"
            ) for i in all_product],
            style = "grid-template-columns: 1fr 1fr 1fr 1fr;"
        ),
        style = "grid-template-columns: 25% 70%"
    )
    page = Main(
        head,
        body,
        style = configHeader
    )
    return page
    