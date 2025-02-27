import sys, os
from fasthtml.common import *
main_path = os.path.dirname(__file__) + "\\asset"
# file_path = os.path.join(main_path, '/asset')
# print(main_path, file_path)

cartpng = "cart_removebg_preview.png"

print(cartpng)

configHeader = "padding-top: 0px;"
headerfontStyle = """   color: #ffffff
                        """
ButtonHeaderStyle = "margin-right: 10px;"
CheckingStyle = "border: solid;"
def Header():
    page = Div(
            A(
                H1(
                    "Teerawee Shop",
                    Style = headerfontStyle
                ), 
                href='/', 
                Style="""
                    text-decoration: none;
                    margin-left: 20px;
                """ + ButtonHeaderStyle
            ),
            Form(
                Input(
                    placeholder = "search...",
                    style = "margin: 0px;"
                    ),
                style = "margin: 0px;"
                ),
            Div(
                A(
                    Img(
                        src = cartpng,
                        style = "height: 100px;"
                    ),
                    href = "/cart",
                    style = ButtonHeaderStyle
                ),
            ),
            Style="""
                background-color: #073763; 
                height: 80px; 
                width: 100%; 
                z-index: 1000; 
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); 
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
                """
        )
    return page

def TitleHeader(text):
    return H1(text, 
              Style="""padding-top: 30px; 
              margin-left: 15%; 
              display: flex;"""
              ),
    