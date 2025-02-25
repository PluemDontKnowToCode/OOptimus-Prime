from fasthtml.common import *
from backend.lib255 import *
from Component import *
address = [
    {"district": "XYZ","province":"Baan Opor","zip_code":"61000","phone":"0845658790"},
    {"district": "ABC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"}
]
def PurchasePage():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),

        Div(
            H1(
                "Address",
            ),
            Group(*
                [
                    Card(
                        Div(f"district : {i['district']}"),
                        Div(f"province : {i['province']}"),
                        Div(f"zip code : {i['zip_code']}"),
                        Div(f"phone : {i['phone']}"),
                        Style=("width:100px;justify-content: space-between;border: solid; align-items: center;"),
                        
                    )
                    for i in address
                ],
            ),
            cls="address",
            Style="padding-top: 100px;"
        ),
        #Style="background-color: #f5f5f5;"
    )
    return page