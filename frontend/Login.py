from fasthtml.common import *
from backend.lib255 import *
import Component
from _main import *

def Page():
    page = Title("Login - Teerawee Shop"),Main(
        Component.Header(False),
        Div(
            H1(
                "Welcome To Teerawee Shop",
                Style = " margin-left: center; text-align: center; margin-top: 20px;"
            ),
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
                        Button(
                            "Sign In",
                            style = "justify-self: center;"
                            ),
                        method = "get",
                        action = '/login_process',
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
            
            A(
                
                style="width: 40%; margin: 0 auto; padding-top: 10%; display: flex; justify-content: center;",
            ),
            Div(
                Span("Don't Have an Account? "),
                A("Sign Up", href="register", style="color: blue; text-decoration: none;"),
                style="text-align: center; padding-top: 10px;"
            ),
            Style=""" 
                margin: 0 auto;
                justify-content: center; 
                align-items: center; 
                height: 100vh;
                width: 100%;
            """
        ),
        
        Style="""
            
            padding: 0; 
        """
    )
    return page