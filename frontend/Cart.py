from fasthtml.common import *
import Object

from Object import Product

products = [
   {"name": "Laptop", "description": "High performance laptop"},
   {"name": "Mouse", "description": "Wireless mouse"},
   {"name": "Keyboard", "description": "Mechanical keyboard"}
]

def Page():
    page = Title("Cart - Teerawee Shop"), Main(
        Div(
            A(
                H1("Teerawee Shop"), 
                href='/',
            ),
            Style="background-color: #1ff1ff; width: 100%; position: fixed; top: 0; left: 0; z-index: 1000; box-shadow: 0 2px 4px rgba(0, 0, 0, 1);"
        ),
        
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
            for p in products
            ],
            
        ),
        Style="padding-top: 120px;",
        
    )
    return page