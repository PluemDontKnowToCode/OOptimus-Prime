from fasthtml.common import *
import Component

def Page():
    # part1 = Title("Seller's Home - Teerawee Shop")
    part1 = Component.Header(False)
    part2 = Container(
        # หัวข้อหลัก
        H1("Your Stock", style="text-align: center; color: #2196f3; margin: 20px 0;"),
        
        Grid(
            # Card ที่ 1 - แสดงการจัดการ Text และ Border
            Card(
                H3("Text and Border Styles", style="color: #1976d2;"),
                P("This text is centered with custom font styles", 
                  style="text-align: center; font-size: 16px; line-height: 1.5;"),
                P("Different border styles below"),
                style="""
                    border: 2px solid #2196f3;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 10px;
                """
            ),

            # Card ที่ 2 - แสดงการใช้สีและเงา
            Card(
                H3("Colors and Shadows", style="color: #4caf50;"),
                P("Card with background color and shadow"),
                Button("Hover Me", 
                    style="cursor: pointer;",
                    hx_on="mouseenter: this.style.backgroundColor = '#e8f5e9';\
                          mouseleave: this.style.backgroundColor = '';"
                ),
                style="""
                    background-color: #f5f5f5;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    padding: 20px;
                    margin: 10px;
                """
            ),

            # Card ที่ 3 - แสดงการจัดการขนาด
            Card(
                H3("Size Management", style="color: #ff5722;"),
                P("This card has specific dimensions"),
                style="""
                    width: 100%;
                    min-height: 200px;
                    padding: 20px;
                    margin: 10px;
                    background-color: #fff3e0;
                """
            ),

            # Card ที่ 4 - แสดงการจัดการ margin และ padding
            Card(
                H3("Spacing Demo", style="color: #9c27b0;"),
                P("Different margin and padding"),
                Div("Inner content", 
                    style="background-color: #f3e5f5; padding: 10px; margin: 10px;"),
                style="""
                    margin: 10px;
                    padding: 20px;
                    border: 1px dashed #9c27b0;
                """
            )
        ),

        # เพิ่มส่วนอธิบาย
        Card(
            H3("Style Reference", style="color: #333;"),
            P("Common styles used in this example:"),
            Ul(
                Li("text-align: center - จัดตำแหน่งข้อความ"),
                Li("margin & padding - ระยะห่างภายนอกและภายใน"),
                Li("border - การจัดการเส้นขอบ"),
                Li("background-color - สีพื้นหลัง"),
                Li("box-shadow - เงาของกล่อง"),
                Li("width & height - ขนาดความกว้างและสูง"),
                style="list-style-type: disc; margin-left: 20px;"
            ),
            style="""
                margin-top: 20px;
                padding: 20px;
                background-color: #fafafa; 
            """
        )
    )
    
    page = Main(
        part1,
        part2,
        Script(Component.get_warn_js()),
        style = Component.configHeader
    )
    return page