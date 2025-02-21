from fasthtml.common import *
import Object

from Object import Product
cart = [
   {"name": "Laptop", "description": "High performance laptop","price": 300},
   {"name": "Mouse", "description": "Wireless mouse","price": 300},
   {"name": "Keyboard", "description": "Mechanical keyboard","price": 300}
]

price = sum(item["price"] for item in cart)
def Page():
    page = Title("Cart - Teerawee Shop"), Main(
        Div(
            A(
                H1("Teerawee Shop"), 
                href='/',
            ),
            Style="background-color: #1ff1ff; width: 100%; position: fixed; top: 0; left: 0; z-index: 1000; box-shadow: 0 2px 4px rgba(0, 0, 0, 1);"
        ),
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
                        
                        P("Description:"),
                        Div(
                            p["description"],
                            Style="width:200px;"
                        )
                    ),
                    Style="display: flex; justify-content: space-between; width: 500px;, boarder : solid;"
                
                )
                for p in cart
            ],
            
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
            Style="padding-top: 120px; display: flex; justify-content: space-between; , boarder : solid;",
        ),
        
        
    )
    return page