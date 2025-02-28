from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page(account_inst):
    part_header = Component.Header()
    part_body = Card(
        
        style = "border: solid;"
    )
    page = Main(
        part_header,
        part_body,
        style = Component.configHeader
    )
    return page