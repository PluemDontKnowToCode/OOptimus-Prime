from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page():
    current_account = market1.current_account
    part_header = Component.Header(False)
    part_body = Card(
        
        style = "border: solid;"
    )
    page = Main(
        part_header,
        part_body,
        style = Component.configHeader
    )
    return page