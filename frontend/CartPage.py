from fasthtml.common import *
from backend.lib255 import *
from Component import *
from _main import app

cart = [
   {"name": "Laptop", "description": "High performance laptop","price": 300},
   {"name": "Mouse", "description": "Wireless mouse","price": 600},
   {"name": "Keyboard", "description": "Mechanical keyboard XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","price": 300}
]

price = sum(item["price"] for item in cart)
lenCart = len(cart)

def Page():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),
        TitleHeader("Your Cart"),
        Div(
            UpdateCartUI(),
            Div(
                Card(
                    P(
                        "Order Summary",
                    ),

                    Div(f"Total: {price}",
                        cls="price",
                        id="price"
                    ),
                    Style='width: 500px;'
                ),
                A(Button(
                    f"Check Out ({lenCart})"),
                    href="/purchase",
                    cls="lenCart",
                    id ="lenCart"
                ),
            ),
            Style=" display: flex; justify-content: space-between; , boarder : solid; padding-top: 20px;",
        ),
        #Style="background-color: #f5f5f5;"
        Style="padding:0;"
    )
    return page
#delete card code
@app.delete("/cart/remove/{name}")
async def Remove(name : str):
    print(name + " : Click!!"), 

    global cart
    
    cart = [item for item in cart if item["name"] != name]
    price = sum(item["price"] for item in cart)
    lenCart = len(cart)

    return Div(
        Button(f"Check Out ({lenCart})", id="lenCart", hx_swap_oob="true"),
        Div(f"Total: {price}", id="price", hx_swap_oob="true"),
        UpdateCartUI()
    ),
    
def UpdateCartUI():
    if(len(cart) != 0):
        return Div(*
            [
                Card(
                    Div(
                        Img(
                            src="https://glassmania.com/media/catalog/product/cache/c2977421f383e646049de5ab98da7a5c/n/s/nspf50bobl_5.png",
                            Style="width: 200px;"
                        ),
                    ),
                    Div(
                        Div(H3(p["name"])),
                        Div(
                            p["description"],
                            Style="width:500px;"
                        ),
                        Div(
                            f"Price: ${p['price']}",
                            Style="padding-top: 10px;"
                        )
                    ),
                    Div(
                        Button(
                            "X",
                            hx_delete=f"/cart/remove/{p['name']}",
                            hx_target=f"#{p['name']}",  # Ensures only the nearest div (the card) is removed
                            hx_swap="outerHTML"
                        ),
                    ),
                    id = p["name"],
                    Style="display: flex; justify-content: space-between; width: 750px; border: ridge; align-items: center;"
                )
                for p in cart
            ],
            cls="product_list",
            id="product_list",
            hx_swap_oob="true",
            Style="margin-left: 5%;"
        )
    return Div("Nothing Here", 
               id="product_list",
               Style="align-items: center;",
               hx_swap_oob="true"
            )

