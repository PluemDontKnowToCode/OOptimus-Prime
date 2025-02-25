from fasthtml.common import *
from ItemDetail import *
def Page():
    return Main(
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