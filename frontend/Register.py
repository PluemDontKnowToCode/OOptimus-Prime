from fasthtml.common import *
from backend.lib255 import *
import Component

def page():
    part_header = Component.Header(False, False, "Register")

    page = Title("Register - Teerawee Shop"), Main(
        part_header,
        H1("Sign Up",style="width: 150px; margin: 0 auto; padding-top: 2%;"),
        Div(
            Div(
                Form(
                    Label("Choose Your Role"),
                    Div(
                        Label(Input(type = "radio", name = "role", value = "customer", checked = "true"), "Customer"),
                        Label(Input(type = "radio", name = "role", value = "seller"), "Seller"),
                        style = "margin-bottom: 2%;"
                    ),
                    Input(
                        placeholder = "username...",
                        id = "name",
                        style = "margin-bottom: 2%;"
                        ),
                    Input(
                        placeholder = "password...",
                        id = "password",
                        style = "margin-bottom: 2%;"
                        ),
                    Input(
                        placeholder = "repeat password...",
                        id = "r_password",
                        style = "margin-bottom: 2%;"
                        ),
                    Button(
                        "Sign Up",
                        style = "justify-self: center;"
                        ),
                    method = "post",
                    action = '/register',
                    style = "margin: 0px; padding-top: 8%;"
                )
            ),
            # Div(
            #     Form(
            #         style = "margin: 0px; "
            #         ),
            # ),
            style="width: 40%; margin: 0 auto; padding-top: 10%;"
        ),
        style = Component.configHeader
    )
    return page

def validate_register(name : str, password : str, r_password : str, role : str):
    if(password != r_password):
        return 'error'
    if role == "customer":
        new_account = Customer(id=market1.generate_id(1),name=  name,username= name,password= password, money =10000, market= market1)
    elif role == "seller":
        new_account = Seller(id=market1.generate_id(2),name=  name,username= name,password= password, money =10000, market= market1)
        
    market1.update_current_user(new_account)
    market1.add_account(new_account)
    return "success"