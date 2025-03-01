from fasthtml.common import *
import Component

def page():
    part_header = Component.Header()

    page = Main(
        part_header,
        style = Component.configHeader
    )
    return page