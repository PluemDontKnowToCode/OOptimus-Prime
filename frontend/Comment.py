from fasthtml.common import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fasthtml.common import *
from backend.lib255 import *

def insert_comment(user_id: str, star: int, new_comment: str):
    name = market1.current_account.name
    c = Comment(name, new_comment, star, user_id)