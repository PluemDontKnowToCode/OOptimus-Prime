from fasthtml.common import *


def HomePage():
    return Container(
        H1("Our Website"),

        Container(
            H2("Section 1"),
            P("Content for section 1"),
            Button("Learn More"),
            style="text-align: left; background-color: #f0f0f0;"
        ),
        Container(
            H2("Section 2"),
            P("Content for section 2"),
            Button("Read More"),
            style="text-align: right; background-color: #e0e0e0;"
        )
    )