from fasthtml.common import *
from backend.lib255 import *
from Component import *
from _main import *

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

coupon = [
    {
        "discount_percent": 10,
        "less_amount": 199,
        "product_count": 5,
        "start_time": "2025-03-02",
        "end_time": "2025-03-11"
    },
    {
        "discount_percent": 20,
        "less_amount": 299,
        "product_count": 3,
        "start_time": "2025-04-01",
        "end_time": "2025-04-10"
    }
]
cart = [
    {"name": "Laptop", "description": "High performance laptop","price": 300},
    {"name": "Mouse", "description": "Wireless mouse","price": 600},
    {"name": "Keyboard", "description": "Mechanical keyboard XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","price": 300}
]
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
                                width: 80%;
                            """
                        ),
                        
                        Style=" display: flex; overflow: hidden; width: 100%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
                
                Div(
                    H3("Available Coupon",Style="margin-left:6%"),
                    Div(
                        Div(*
                        [
                            CouponCard(i["discount_percent"],i["less_amount"],i["start_time"],i["end_time"],product_count=i["product_count"])
                            for i in coupon
                        ],
                            #Style= ("width:900px; border: 1px solid black; display: flex; flex-direction: row; flex-wrap: wrap;"),
                            id="addressSlider",
                            Style="""
                                display: flex; 
                                overflow-x: auto; 
                                scroll-behavior: smooth; 
                                white-space: nowrap; 
                                width: 80%;
                            """
                        ),
                        
                        Style="display: flex; overflow: hidden; width: 100%;margin-left: 2%"
                    ),
                    cls="address",
                    Style="padding-top: 1%;"
                ),
                Style="width: 70%;"
            ),
            Div(
                Div(*
                [
                    Card(
                        Img(
                            src="https://i2.wp.com/images.genshin-builds.com/genshin/characters/klee/image.png?strip=all&quality=75&w=256",
                            Style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;"),
                        Div(f"{i['name']}"),
                        Div(f"${i['price']}"),
                        Style="""
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            width: 100%;
                            max-width: 750px;
                            height: 60px;  /* Fixed height */
                            border: ridge;
                            padding: 10px;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                            border-radius: 10px;
                            background-color: white;
                        """,
                        
                    )
                    for i in cart
                    ],
                
                    Style="width:100%;"
                ),
                Div(
                    Hr(Style="border: none; border-top: 3px dashed black; width: 100%;"),
                ),
                Div(
                    Div(
                        H3("SubTotal"),
                        Div(f"${sum(i['price'] for i in cart)}"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Shipping"),
                        Div(f"$50"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Discount"),
                        Div(f"$0"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    Div(
                        H3("Total"),
                        Div(f"${sum(i['price'] for i in cart) + 50}"),
                        Style="display: flex; justify-content: space-between; width: 100%;",
                    ),
                    cls="total",
                ),
                Div(
                    Hr(Style="border: none; border-top: 3px dashed black; width: 100%;"),
                ),
                Div(
                    "All Products cannot be returned or exchanged",
                    Style="padding-top: 10px; padding-bottom: 10px;"
                ),
                A(
                    Button("Purchase",
                           Style="width: 100%;"
                           
                        ),
                        method = "post",
                        action = f"/purchase/result",
                        Style="padding-top: 10px;"
                ),
                Style="padding-top:0px; width: 25%;"
            ),
            
            Style="display: flex;"
        ),

        
        Style="padding: 0px;",
    )
    return page

def ResultPage(result):
    if(result["success"]):
        page = Title("Cart - Teerawee Shop"), Main(
            Header(),
            TitleHeader("Purchase Result"),
            Div(
                H3("Thank you for your purchase"),
                P("Your order has been placed successfully"),
                Button("Continue Shopping",Style="width: 100%;"),
                Style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 100%;"
            ),
            Style="padding: 0px;",
            
        )
    else:
        page = Title("Cart - Teerawee Shop"), Main(
            Header(),
            TitleHeader("Purchase Result"),
            Div(
                H3("Failed to place order"),
                P("Please try again later"),
                Button("Return to Cart",Style="width: 100%;"),
                Style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 100%;"
            ),
            Style="padding: 0px;",
        )
    return page

def CouponCard(discount, order_min,start_date, end_date,product_count = 0):
    condition = f"Orders ฿{order_min}+"
    if(product_count == 0):
        condition += f" or {product_count} more products"
    return Div(
        H2(f"{discount}% OFF", Style="margin: 0;"),
        P(condition, Style="margin: 0;"),
        Hr(),
        P(f"{start_date} ~ {end_date}", Style="margin: 0 auto;"),
        Button("USE", Style="margin-top: 10px; padding: 5px 15px; border: 1px solid blue; background: white; color: blue;"),
        Style="border: 1px solid black; padding: 15px; width: 200px; text-align: center; display: inline-block; margin: 10px; position: relative;"
    )