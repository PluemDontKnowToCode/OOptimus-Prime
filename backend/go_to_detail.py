from fasthtml.common import *
from lib255 import *

app, rt = fast_app()

market01 = set_up()
user1 = User("Neeko", market01)

@rt('/')
def get():
    plist = market01.product_list
    page = Titled("Teerawee's Shop",
       Div(*[Card(
            Div(
                Div(
                    H3(p.name), 
                    P(p.des)), 
                Div(
                    Form(
                        Button("view detail", type = "summit"),
                        method = "get",
                        action = f"/detail/{p.get_id}"
                        )    
                    ),
                    Style = "display: block; justify-content: space-between;"), 
            Img(src = p.source, Style = "width: 25%; height: auto;"), 
            Style = "display: flex; justify-content: space-between;") for p in plist]))
    # for i in plist:
    #     print(i.get_id)
    return page

@rt('/detail/{p_id}')
def get(p_id: int):
    # print(f"ID: {p_id}, Type: {type(p_id)}")
    list1 = market01.view_product_detail(p_id)
    p, c = list1
    list_dis =["Name", "ID", "Price", "Description"]
    j1 = create_json(list_dis, p)


    part_detail = Titled(
        "Detail",
        Div(
            *[Card(
                Div(
                    f"{i}: {j}"
                )
            ) for i, j in j1.items()]
        )
    )


    part_add_comment = Titled(
        "Add your opinion",
        Form(
            Input(type = "text", id = "new_comment", placeholder = "about your thinking"),
            method = "post",
            action = ""
        )
    )


    part_comment = Titled("Comment")
    if len(c) > 0:
        part_comment = Titled(
            "Comment",
            *[Card(
                Div(
                    Div(
                        f"{lc["name"]}   {lc["star"]}",
                        Card(
                            lc["text"], style = ""
                        )
                    )
                ),
                Style = "width: 50%;"
            ) for lc in c]
        )


    page = Main(
        Div(
            part_detail,
            part_add_comment,   
            part_comment
        )
    )
    return page

@rt("/add_comment/{user_name}/{text}/{star}/{p_id}")
def post(user_name, text, star, p_id):
    com1 = Comment(user_name, text, star)
    market01.add_comment_to_product(p_id, com1)
    


serve()