from fasthtml.common import *

import os
import dotenv

dotenv.load_dotenv()

def Page():
    
    page = Container(
        A("Our Website", href= os.getenv('HOME')),
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
        ),
        Titled(
            "FastHTML Example",
            Div(
                P("นี่คือย่อหน้า"),
                A("ไปที่เว็บไซต์", href="https://example.com"),
                Img(src="https://example.com/image.jpg", alt="ตัวอย่างภาพ"),
                Table(
                    Tr(
                        Th("หัวข้อ 1"),
                        Th("หัวข้อ 2")
                    ),
                    Tr(
                        Td(Span("ข้อมูล 1", cls="highlight")),  
                        Td("ข้อมูล 2")
                    ),
                    Tr(
                        Td("ข้อมูล 3"),
                        Td(Span("ข้อมูล 4 (สำคัญ)", cls="important")),  
                ),
                Div(P("เนื้อหาใน Div"), cls="box")
                )
            )
        )
    )
    
    return page