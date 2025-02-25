from fasthtml.common import *
from backend.lib255 import *
from Component import *
address = [
    {"district": "XYZ","province":"Baan Opor","zip_code":"61000","phone":"0845658790"},
    {"district": "ABC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "AAC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "AXC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "AXC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "AXC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "AXC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"},
    {"district": "KKC","province":"Baan Opor","zip_code":"25410","phone":"0836694812"}
]
def PurchasePage():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),

        Div(
            H1(
                "Address",
            ),
            Div(
                Div(*
                [
                    Card(
                        Div(f"district : {i['district']}"),
                        Div(f"province : {i['province']}"),
                        Div(f"zip code : {i['zip_code']}"),
                        Div(f"phone : {i['phone']}"),
                        Style=("width:200px;margin-left:10px;justify-content: space-between;border: solid;"),
                        
                    )
                    for i in address
                ],
                #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row;"),
                id="box"
                ),
                Button("⬅", 
                    onclick="scrollSlider(-1)", 
                    Style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); z-index: 10;"
                ),
                cls="address-grid",
            ),
            
            cls="address",
            Style="padding-top: 100px;"
        ),
        #Style="background-color: #f5f5f5;"
    )
    return page