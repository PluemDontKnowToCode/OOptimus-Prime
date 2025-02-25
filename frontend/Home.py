from fasthtml.common import *
from ItemDetail import *
from Component import *
def Page():
    head = Header()
    body = Div(
        H1("This is heading 1"),
        P("This is some text."),
        Hr(),
        H2("This is heading 2"),
        P("This is some other text."),
        Hr(),
        H2("This is heading 2"),
        P("This is some other text."),

        A(Button("Click me"),href="/cart")
    )
    page = Main(
        head,
        body,
        style = styheader
    )
    return page
    