from fasthtml.common import *
from backend.lib255 import *
from Component import *
from frontend._main import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def Page():
    head = Component.Header()
    body = Container(
        Div(
            Div(  # ส่วนอัปโหลดรูปภาพ
                Label("Add Picture"),
                Input(type="file", name="product_image"),
                style="width: 200px; height: 200px; border: 1px dashed #aaa; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px;"
            ),
            Form(  # ฟอร์มข้อมูลสินค้า
                Div(Label("Product Name:"), Input(type="text", name="name", id="product_name"), style="margin-bottom: 20px;"),
                Div(Label("Description:"), Textarea(name="description", rows=3, id="description"), style="margin-bottom: 20px;"),
                Div(Label("Price (฿):"), Input(type="number", name="price", step="0.01", id="price"), style="margin-bottom: 20px;"),
                Div(Label("Quantity:"), Input(type="number", name="quantity", min=1, value=1, id="quantity"), style="margin-bottom: 20px;"),
                Div(Button("Confirm", type="button", onclick="submitForm()"), style="margin-top: 20px;"),
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


def insert_request(p_id: str, name: str, description: str, price: str, quantity: str):
    seller_id = market1.current_account.id
    product = Product(name, market1.generate_product_id(), price ,description, img1="", category="", stock = quantity,market =  market1)
    r = RequestedProduct(product, market1.current_account)
    market1.add_comment_to_product(p_id, r)
    return Redirect(f'/requestproduct/{p_id}')