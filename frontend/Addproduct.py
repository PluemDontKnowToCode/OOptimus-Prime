from fasthtml.common import *
from backend.lib255 import *
from Component import *
from frontend._main import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def Page():
    head = Component.Header(False, False, "")
    body = Container(
        Div(
            Form(  # ฟอร์มข้อมูลสินค้า
                Div(Label("Product Name:"), Input(type="text", name="name", id="product_name"), style="margin-bottom: 20px;"),
                Div(Label("Description:"), Textarea(name="description", rows=3, id="description"), style="margin-bottom: 20px;"),
                Div(Label("Price (฿):"), Input(type="number", name="price", step="1", id="price"), style="margin-bottom: 20px;"),
                Div(Label("Quantity:"), Input(type="number", name="quantity", min=1, value=1, id="quantity"), style="margin-bottom: 20px;"),
                Div(Label("Category (use only English):"), Input(type="text", name="category", id="category"), style="margin-bottom: 20px;"),
                Div(Label("Image URL:"), Input(type="text", name="image_url", id="image_url"), style="margin-bottom: 20px;"),
                Div(Button("Confirm"), style="margin-top: 20px;"),
                method="post",
                action="/addrequestproduct",
                id="product_form",
                style="text-align: left; padding: 20px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"
            ),
            style="justify-content: center; align-items: center; height: 100vh; width: 100%;"
        ),
        className="container"
    )

    page = Main(
        head,
        body,
        Component.warn_to_login_modal,
        Script(Component.get_warn_js()),
        style = Component.configHeader
    )

    return page


def insert_request(p_id: str, name: str, description: str, price: str, quantity: str, category: str, image_url: str):
    seller_id = market1.current_account.id
    product = Product(name, market1.generate_id(0), price ,description, img1=image_url, category=category, stock = quantity,market =  market1)
    r = RequestedProduct(product, market1.current_account)
    market1.add_requested(p_id, r)
    return Redirect(f'/')