from fasthtml.common import *

def Home():
    return Main(
        P('Hello World!'), hx_get="/change"
    ) 