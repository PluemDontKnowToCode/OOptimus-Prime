from fasthtml.common import *
import Component

def Page():
    part_header = Component.Header()
    page = Main(
        part_header,
        style = Component.configHeader
    )
    return page