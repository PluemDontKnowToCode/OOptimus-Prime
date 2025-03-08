from fasthtml.common import *
import Component
import os
import dotenv

dotenv.load_dotenv()

def Page():
    page = Title("Admin - Teerawee Shop"), Main(
        Component.Header(False, False, "Admin"),
        Grid(
            Div(
                Div(
                    H1(
                        "manage coupon",
                        Style="margin: 2%;"
                    ),
                    Div(
                        Button(
                            "Create coupon",
                            hx_get="/admin/createCoupon"
                        ),
                        Style="margin: 2%;"
                    ),
                    
                    Style="""
                        display: flex; 
                        justify-content: space-between;
                        
                    """,
                    id="manage_coupon_head",
                ),
                Div(
                    id="manage_coupon_body",
                    style = "height: 20vw;"
                ),
                Style="padding-top:0px;"
            ),
            Div(
                Div(
                    H1(
                        "manage event",
                        Style="margin: 2%;"
                    ),
                    Div(
                        Button(
                            "Create event",
                            hx_get="/admin/createEvent"
                        ),
                        Style="margin: 2%;"
                    ),
                    
                    Style="""
                        display: flex; 
                        justify-content: space-between;
                        
                    """,
                    id="manage_event_head",
                ),
                Div(
                    id="manage_event_body",
                    style = "height: 20vw;"
                ),
            ),
            Style = """
                grid-template-columns: 1fr;
                grid-template-rows: 1fr 1fr;
                
            """
        ),
        Script(Component.get_warn_js()),
        Style=Component.configHeader
    )
    
    return page


def manageCouponCard():

    return 