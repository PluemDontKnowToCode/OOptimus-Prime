from fasthtml.common import *
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *
import Component

def transaction_modal_script(count):
    scr = f"""
        const open_transaction_{count} = document.querySelector(".transaction_modal{count}")
        const close_transaction_{count} = document.querySelector(".close_transaction_modal{count}")
        const transaction_show_modal_{count} = document.querySelector(".transaction_main_modal_{count}")

        open_transaction_{count}.addEventListener("click", () => {{
            transaction_show_modal_{count}.showModal()
        }})

        close_transaction_{count}.addEventListener("click", () => {{
            transaction_show_modal_{count}.close()
        }})
"""
    return scr

def create_modal(data, count, net_price):
    res = Dialog(
        Div(
            *[Div(H2(i)) for i in data],
            Div(H1(f"Total {net_price}฿")),
            style = "flex-direction: column;"
        ),
        Div(
            Button(
                "X", 
                cls = f"close_transaction_modal{count}"
            )
        ),
        cls = f"transaction_main_modal_{count}"
    )

    return res

def create_card(count, date, data, net_price):
    res = Card(
        f"Bill #{count}",
        Div(date),
        Button("Show", cls = f"transaction_modal{count}"),
        create_modal(data, count, net_price),
        Script(transaction_modal_script(count))
    )
    return res

def Page():
    transaction_list = market1.get_transaction_list()
    # print(f"transaction list: {transaction_list}")
    card = []
    if len(transaction_list) > 0:
        for i in range(len(transaction_list)):
            card.append(create_card(i, transaction_list[i].date, transaction_list[i].data, transaction_list[i].net_price))
    
    page = Div(
        Component.Header(False, HeaderText = "Transaction"),
        Div(
            *card
        ),
        Script(Component.get_warn_js()),
    )

    return page