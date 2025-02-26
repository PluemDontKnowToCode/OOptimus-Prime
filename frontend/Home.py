from fasthtml.common import *
from ItemDetail import *
from Component import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def Page():
    head = Header()
    body = Grid(
        Div(
            Div(
                "Category",
                style = "text-align: center;"
            ),
            style = CheckingStyle
        ),
        Grid(
            *[Card(
                f"subDiv {i}",
                style = CheckingStyle + "height: 100px;"
            ) for i in range(50)],
            style = "grid-template-columns: 1fr 1fr 1fr 1fr;"
        ),
        style = "grid-template-columns: 25% 70%"
    )
    page = Main(
        head,
        body,
        style = configHeader
    )
    return page
    