
from fasthtml.common import *

import Admin
import Home

app, rt = fast_app()

@rt('/')
def get():
    return Home.Page()

@rt('/change')
def get():
    return Admin.HomePage()

serve()