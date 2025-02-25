from fasthtml.common import *
configHeader = "padding-top: 0px;"
headerfontStyle = """   color: #ffffff
                        """
ButtonHeaderStyle = "margin-right: 10px;"
CheckingStyle = "border: solid;"
def Header():
    return Div(
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
            A(
                Button(
                    "Cart"
                ),
                href = "/cart",
                style = ButtonHeaderStyle
            ),
            Style="""
                background-color: #073763; 
                height: 80px; 
                width: 100%; 
                z-index: 1000; 
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); 
                display: flex; 
                align-items: center;
                """
        )

def TitleHeader(text):
    return H1(text, 
              Style="""padding-top: 30px; 
              margin-left: 15%; 
              display: flex;"""
              ),