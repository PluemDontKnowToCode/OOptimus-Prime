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
                            style = "margin: 0px;"
                            ),
                        style = "margin: 0px; padding-top: 8%;"
                        ),
                ),
                Div(
                    Form(
                        Input(
                            placeholder = "password...",
                            style = "margin: 0px;"
                            ),
                        style = "margin: 0px; "
                        ),
                ),
                style="width: 40%; margin: 0 auto; padding-top: 10%;"
            ),
            
            A(
                Button("Sign In"),
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