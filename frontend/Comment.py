from fasthtml.common import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fasthtml.common import *
from backend.lib255 import *

def insert_comment(p_id: str, star: int, new_comment = "None"):
    user_id = market1.current_account.id
    name = market1.current_account.name
    c = Comment(name, new_comment, star, user_id)
    market1.add_comment_to_product(p_id, c)
    return Redirect(f'/detail/{p_id}')