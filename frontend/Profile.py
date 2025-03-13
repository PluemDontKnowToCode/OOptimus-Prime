from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page():
    role_bool = isinstance(market1.current_account, Customer)
    current_account = market1.current_account
    profile_image_url = current_account.image  
    username = current_account.name 
    money = current_account.money
    if role_bool: coupon_list = current_account.coupon_list 

    part_header = Component.Header(False)
    
    left_menu = Div(
        Button(
            "Profile", 
            type="button", 
            onclick="showContent('profile')",  
            style="margin-top: 10px; width: 100%;"
        ),
        Button(
            "Transaction", 
            type="button", 
            onclick="window.location.href = '/transaction'",  
            style="margin-top: 10px; width: 100%;"
        ) if role_bool else Div(),
        Button(
            "Coupon", 
            type="button", 
            onclick="showContent('coupon')",  
            style="margin-top: 10px; width: 100%;"
        ) if role_bool else Div(),
        Button(
            "Address",
            type="button",
            onclick="window.location.href = '/address'",
            style="margin-top: 10px; width: 100%;"
        ) if role_bool else Div(),
        style="display: flex; flex-direction: column; gap: 10px; width: 250px; padding: 10px; border-right: solid 1px #ccc; height: 100vh;background-color: #555555;"
    )

    content_area = Div(
        Div(
            Card(
                Img(
                    src=profile_image_url,
                    id="profileImage",
                    style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover;"
                ), 
                Div(
                    f"{username}",
                    id="usernameDisplay",
                    style="text-align: center; font-size: 18px; margin-top: 10px;"
                ),
                Div(
                    Button(
                        "Change username", 
                        type="button",
                        id="changeUsernameButton",
                        onclick="toggleUsernameEdit()",
                        style="margin-top: 10px; margin-right: 10px;"
                    ),
                    Button(
                        "Change profile", 
                        type="button", 
                        id="changeProfileButton",
                        onclick="document.getElementById('fileInput').click();",
                        style="margin-top: 10px;"
                    ),
                    style="display: flex; gap: 10px; align-items: center;"
                ), 
                Div(
                    f"Money :{money} Baht",
                    id="moneyDisplay",
                    style="text-align: center; font-size: 18px; margin-top: 10px;"
                ),
                Form(
                    Input(
                        type="text", 
                        name="new_username",
                        id="usernameInput",
                        value=username,
                        style="display: none; text-align: center; font-size: 18px; padding: 5px; width: 200px;"
                    ),
                    Button(
                        "Save",
                        type="submit",
                        id="saveUsernameButton",
                        style="display: none; margin-top: 5px;"
                    ),
                    method="post",
                    action="/profile/change_name/",
                    style="display: flex; flex-direction: column; gap: 5px; align-items: center; margin-top: 10px;",
                ),
                Input(
                    type="file",
                    id="fileInput",
                    onchange="updateProfileImage(event)",
                    style="display: none;"
                ),
                style="border: solid; padding: 20px; display: flex; flex-direction: column; align-items: center; gap: 10px;"
            ),
            id="profileContent",
            style="display: block;"
        ),
        
        Div(
            "Transaction history...",
            id="transactionContent",
            style="display: none;"
        ),
        
        Div(
            Div(
                *[
                    Div(
                        H1(f"{coupon.id}", style="margin-top: 20px; padding: 10px; font-weight: bold;"),
                        Ul(
                            Li(f"Discount: {coupon.discount_percent}%"),
                            Li(f"Least Cost: ${coupon.less_amount}"),
                            Li(f"Least Amount: {coupon.product_count}"),
                            Li(f"Date Begin: {coupon.start_time}"),
                            Li(f"Date Expire: {coupon.end_time}"),
                            style="list-style-type: none; padding: 20; margin: 10px 0;"
                        ),
                        Button(
                            "Use",
                            type="button",
                            onclick="window.location.href='http://localhost:3000/cart';",
                            style="margin-top: 10px; padding: 10px; border: none; border-radius: 5px; cursor: pointer;"
                        ),
                        style="margin-top: 10px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; width: 300px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);"
                    ) for coupon in coupon_list
                ],
                id="couponContent",
                style="display: none; flex-direction: row; gap: 20px; margin-top: 20px; flex-wrap: wrap;"
            ),
        ) if role_bool else Div(),
        style="flex-grow: 1; padding: 20px;"
    )

    main_content = Div(
        left_menu,
        content_area,
        style="display: flex; height: 100vh;"
    )

    script = ("""
    function showContent(contentType) {
        document.getElementById('profileContent').style.display = 'none';
        document.getElementById('transactionContent').style.display = 'none';
        document.getElementById('couponContent').style.display = 'none';

        if (contentType === 'profile') {
            document.getElementById('profileContent').style.display = 'block';
        } else if (contentType === 'transaction') {
            document.getElementById('transactionContent').style.display = 'block';
        } else if (contentType === 'coupon') {
            document.getElementById('couponContent').style.display = 'flex';
            document.getElementById('couponContent').style.flexDirection = 'row';
        }
    }

    function toggleUsernameEdit() {
        var usernameInput = document.getElementById('usernameInput');
        var saveButton = document.getElementById('saveUsernameButton');
        var usernameDisplay = document.getElementById('usernameDisplay');

        if (usernameInput.style.display === 'none') {
            usernameInput.style.display = 'block';
            saveButton.style.display = 'block';
            usernameDisplay.style.display = 'none';
        } else {
            usernameInput.style.display = 'none';
            saveButton.style.display = 'none';
            usernameDisplay.style.display = 'block';
        }
    }

    function saveUsername(event) {
        event.preventDefault();

        var formData = new FormData();
        formData.append("new_username", document.getElementById("usernameInput").value);

        fetch("/profile/change_name/", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("usernameDisplay").innerText = data.new_username;
                alert("Username updated successfully!");
                window.location.href = "/profile";
            } else {
                alert("Update failed! " + (data.message || ""));
            }
        })
        .catch(error => console.error("Error:", error));
    }

    function updateProfileImage(event) {
        var file = event.target.files[0];
        if (!file) {
            alert("No file selected!");
            return;
        }

        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('profileImage').src = e.target.result;
        };
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            var base64String = reader.result.replace("data:", "").replace(/^.+,/, "");

            var formData = new FormData();
            formData.append("file", base64String);
            formData.append("filename", file.name);

            fetch("/profile/update_image", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('profileImage').src = data.image_url;  // Update to the URL from the server
                    alert("Profile image updated successfully!");
                } else {
                    alert("Upload failed: " + data.message);
                }
            })
            .catch(error => console.error("Error:", error));
        };
    }
    """)
    script += Component.get_warn_js()

    page = Main(
        part_header,
        main_content,
        Script(script),
        style=Component.configHeader
    )
    
    return page