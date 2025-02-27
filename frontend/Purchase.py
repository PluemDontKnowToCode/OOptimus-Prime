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

coupon = {
    
}
def PurchasePage():
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),
        TitleHeader("Purchase"),
        Div(
            Div(
                Div(
                    H3("Address",Style="margin-left:6%"),
                    Div(
                        Div(*
                        [
                            Card(
                                Div(f"district : {i['district']}"),
                                Div(f"province : {i['province']}"),
                                Div(f"zip code : {i['zip_code']}"),
                                Div(f"phone : {i['phone']}"),
                                Style="""
                                    width:200px; 
                                    margin-left:10px;
                                    justify-content: space-between;
                                    border: groove;
                                """,
                                
                            )
                            for i in address
                        ],
                            #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                            id="addressSlider",
                            Style="""
                                display: flex; 
                                overflow-x: auto; 
                                scroll-behavior: smooth; 
                                white-space: nowrap; 
                                border: outset;
                                width: 80%;
                            """
                        ),
                        
                        Style=" display: flex; overflow: hidden; width: 48%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
                
                Div(
                    H3("Coupon",Style="margin-left:6%"),
                    Div(
                        Div(*
                        [
                            Card(
                                Div(f"district : {i['district']}"),
                                Div(f"province : {i['province']}"),
                                Div(f"zip code : {i['zip_code']}"),
                                Div(f"phone : {i['phone']}"),
                                Style="""
                                    width:200px; 
                                    margin-left:10px;
                                    justify-content: space-between;
                                    border: groove;
                                """,
                                
                            )
                            for i in address
                        ],
                            #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                            id="addressSlider",
                            Style="""
                                display: flex; 
                                overflow-x: auto; 
                                scroll-behavior: smooth; 
                                white-space: nowrap; 
                                border: outset;
                                width: 80%;
                            """
                        ),
                        
                        Style=" display: flex; overflow: hidden; width: 48%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
            
            ),
        ),

        
        Style="padding: 0px;",
    )
    return page
