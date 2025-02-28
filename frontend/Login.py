from fasthtml.common import *
from backend.lib255 import *
from Component import *
from _main import *

def Page():
    page = Title("Login - Teerawee Shop"),Main(
        Header(),
        Div(
            H1(
                "Welcome To Teerawee Shop",
                Style = " margin-left: center; text-align: center;"
            ),
            Div(
                Div(
                    Form(
                        Input(
                            placeholder = "username...",
                            id = "name",
                            style = "margin: 0px;"
                            ),
                        Input(
                            placeholder = "password...",
                            id = "password",
                            style = "margin: 0px;"
                            ),
                        Button("Sign In"),
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