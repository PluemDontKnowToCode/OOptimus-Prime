import sys, os
from fasthtml.common import *
main_path = os.path.dirname(__file__) + "\\asset"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.lib255 import *
# file_path = os.path.join(main_path, '/asset')
# print(main_path, file_path)

cartpng = "/cart_removebg_preview.png"
userpng = "/user_imgpng.png"

# print(cartpng)

configHeader = "padding-top: 0px;"
headerfontStyle = """   color: #ffffff
                        """
ButtonHeaderStyle = "margin-right: 10px;"
CheckingStyle = "border: solid;"

login_bool = True

before_add_to_cart_script = """
        const openButton = document.querySelector(".b11")
        const closeButton = document.querySelector(".b2")
        const modal = document.querySelector(".d3")
        
        openButton.addEventListener("click", () => {
            modal.showModal()
        })
        
        closeButton.addEventListener("click", () => {
            modal.close()
        })
"""
add_to_cart_script = """
        const openButton = document.querySelector(".b10")
        const closeButton = document.querySelector(".b2")
        const modal = document.querySelector(".d1")
        
        openButton.addEventListener("click", () => {
            modal.showModal()
        })
        
        closeButton.addEventListener("click", () => {
            modal.close()
        })
    """

alret_scirpt = ""

warn_to_login_modal = Dialog(
                    Div(
                        Div(
                            "Not login Yet",
                            style = "margin-bottom: 20px;"
                        ),
                        Div(
                            A(
                                Button(
                                    "Go to Login"
                                ),
                                href = "/login",
                                style = "margin-right: 20px; text-decoration: none; background-color: #eee;"
                            ),
                            Button(
                                "Continue as guest",
                                cls = "b2"
                            ),
                            style = "blackground-color: white;"
                        ),
                         
                    ),
                    id = "d2",
                    style = "height: 200px; width: 400px;"   
                )

def validate_value():
    current_account = market1.current_account
    global alret_scirpt, login_bool
    login_bool = True if current_account else False
    if not login_bool:
        alret_scirpt = """
        const openButton = document.querySelectorAll(".a1")
        const closeButton = document.querySelector(".b2")
        const modal = document.getElementById("d2")
        openButton.forEach(button => button.addEventListener("click", () => modal.showModal()))
        closeButton.addEventListener("click", () => {
            modal.close()
        })
    """
    else: alret_scirpt = ""
    
def detail_logic():
    validate_value()
    if login_bool: return add_to_cart_script
    f = before_add_to_cart_script
    return f

def Header():
    validate_value()
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
                        style = "height: 100px;",
                        cls = "a1"
                    ),
                    href = "/cart" if login_bool else "",
                    style = ButtonHeaderStyle
                ),
                A(
                    Img(
                        src = userpng,
                        style = "height: 70px;",
                        cls = "a1"
                    ), 
                    href = "/profile" if login_bool else "",
                    style = ButtonHeaderStyle
                ),
                Dialog(
                    Div(
                        Div(
                            "Not login Yet",
                            style = "margin-bottom: 20px;"
                        ),
                        Div(
                            A(
                                Button(
                                    "Go to Login"
                                ),
                                href = "/login",
                                style = "margin-right: 20px; text-decoration: none; background-color: #eee;"
                            ),
                            Button(
                                "Continue as guest",
                                cls = "b2"
                            ),
                            style = "blackground-color: white;"
                        ),
                         
                    ),
                    id = "d2",
                    style = "height: 200px; width: 400px;"   
                ),
            ),
            Script(alret_scirpt),
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

