from fasthtml.common import *
from backend.lib255 import *
from Component import *
from _main import app

# cart = market1.get_customer_cart(market1.current_account.id)["data"]
p = market1.get_product("P000001")
market1.current_account.cart.add_item(p)

def Page():
    cart = market1.get_customer_cart(market1.current_account)
    page = Title("Cart - Teerawee Shop"), Main(
        Header(),
        TitleHeader("My Shopping Cart"),
        Div(
            UpdateCartUI(cart),
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
        #Style="background-color: #f5f5f5;"
        Style="padding:0;"
    )
    return page

#delete card code
@app.delete("/cart/remove/{id}")
async def Remove(id : str):
    print(id + " : Click!!"), 
    market1.current_account.cart.remove_item(market1.get_product(id))
    
    userCart = market1.get_customer_cart_product(market1.current_account)
    
    if(len(userCart) == 0):
        price = 0
    else:
        price = sum(item["price"] for item in userCart)

    return Div(
        Div("",id=id, hx_swap="outerHTML"),
        Button(f"Check Out ({len(userCart)})", id="lenCart", hx_swap_oob="true"),
        Div(f"Total: {price}", id="price", hx_swap_oob="true"),
        UpdateCartUI()
    ),

@app.post("/cart/add")
async def Add():
    p = market1.get_product("P000001")
    # print(p)
    market1.current_account.cart.add_item(p)

def UpdateCartUI(cart = None):
    if(cart):
        itemDict = cart.get_product
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
                        Div(
                            p["description"],
                            Style="width:500px;"
                        ),
                        Div(
                            f"Price: ${p['price']}",
                            Style="padding-top: 10px;"
                        ),
                        Div(
                            f"Amount: {p['amount']}"
                        )
                    ),
                    Div(
                        Button(
                            "X",
                            hx_delete=f"/cart/remove/{p["id"]}",
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
    return Div("Nothing Here", 
               id="product_list",
               Style="align-items: center;",
               hx_swap_oob="true"
            )

