from fasthtml.common import *
from backend.lib255 import *
from Component import *
from _main  import *
# cart = market1.get_customer_cart(market1.current_user.id)["data"]

def Page():
    cart = market1.get_customer_cart(market1.current_user.id)
    cart.update_self()
    unable_list = cart.get_unavailable_product
    page = Title("Cart - Teerawee Shop"), Main(
        Component.Header(bool_search = False),
        TitleHeader("My Shopping Cart"),
        Div(
            UpdateCartUI(cart.get_available_product) if cart else print("Gak"),
            Div(
                Card(
                    P(
                        "Order Summary",
                    ),

                    Div(f"Total: {sum(i.price for i in cart.get_cart_item)}",
                        cls="price",
                        id="price"
                    ),
                    Style='width: 500px;'
                ),
                A(Button(
                    f"Check Out ({cart.size})"),
                    href="/purchase",
                    cls="lenCart",
                    id ="lenCart"
                ),
            ),
            Style=" display: flex; justify-content: space-between; , boarder : solid; padding-top: 20px;",
        ),
        Div(
            TitleHeader("Unavailable"),
            Div(
                UpdateCartUI(unable_list)
            ),
        ) if len(unable_list) > 0 else Div(),
        Script(Component.get_warn_js()),
        #Style="background-color: #f5f5f5;"
        Style="padding:0;"
    )
    return page


def UpdateCartUI(itemDict):
    if(isinstance(itemDict, list)):
        return Div(*
            [
                Card(
                    Div(
                        Img(
                            src=p['img'],
                            Style="width: 200px;"
                        ),
                    ),
                    Div(
                        Div(H3(p["name"])),
                        # Div(
                        #     p["description"],
                        #     Style="width:500px;"
                        # ),
                        Div(
                            f"Price: ฿{p['price']}",
                            Style="padding-top: 10px;"
                        ),
                        Div(
                            f"Amount: {p['amount']}"
                        )
                    ),
                    Div(
                        Button(
                            "X",
                            hx_delete=f"/cart/remove/{p['id']}",
                            hx_swap="outerHTML"
                        ),
                    ),
                    id = p['id'],
                    Style="display: flex; justify-content: space-between; width: 750px; border: ridge; align-items: center;"
                )
                for p in itemDict
            ],
            cls="product_list",
            id="product_list",
            hx_swap_oob="true",
            Style="margin-left: 5%;"
        )
    return Div("", 
               id="product_list",
               Style="align-items: center;",
               hx_swap_oob="true"
            )

