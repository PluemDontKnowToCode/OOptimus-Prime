from fasthtml.common import *
from ItemDetail import *
from Component import *
def Page():
    head = Header()
    body = Grid(
        Div(
            "Category",
            style = CheckingStyle
        ),
        Grid(
            *[Div(
                f"subDiv {i}",
                style = CheckingStyle
            ) for i in range(50)],
            style = "grid-template-columns: 1fr 1fr 1fr 1fr;"
        ),
        style = "grid-template-columns: 25% 75%"
    )
    page = Main(
        head,
        body,
        style = configHeader
    )
    return page
    