from fasthtml.common import *
from Object import *
from Component import *

cart = [
   {"name": "Laptop", "description": "High performance laptop","price": 300},
   {"name": "Mouse", "description": "Wireless mouse","price": 600},
   {"name": "Keyboard", "description": "Mechanical keyboard XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","price": 300}
]

price = sum(item["price"] for item in cart)
def CartPage():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),
        Div(
            Div(*
            [
                Card(
                    Div(
                        Img(src="https://glassmania.com/media/catalog/product/cache/c2977421f383e646049de5ab98da7a5c/n/s/nspf50bobl_5.png",
                            Style="width: 200px;"
                        ),
                    ),
                    Div(
                        Div(
                            H3(p["name"]),
                        ),
                        Div(
                            p["description"],
                            Style="width:500px;"
                        ),
                        Div(
                            p["price"]
                        )
                    ),
                    Style="display: flex; justify-content: space-between; width: 750px;, boarder : solid;,align-items: center;"
                )
                for p in cart
            ],
            
            cls="product_list",
            ),
            Div(
                Card(
                    P(
                        "Order Summary",
                    ),

                    Div(f"Total: ${price}"),
                    Style='width: 500px;'
                ),
                A(Button(
                    f"Check Out ({len(cart)})"),href="/purchase"
                ),
            ),
            Style=" display: flex; justify-content: space-between; , boarder : solid;",
        ),
        Style="padding-top: 100px; background-color: #f5f5f5;"
        
    )
    return page

def PurchasePage():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),

    )

    return page