from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page():
    current_account = market1.current_account
    profile_image_url = current_account.image  
    username = current_account.username 
    address_list = current_account.address_list
    coupon_list = current_account.coupon_list 

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
            onclick="showContent('transaction')",
            style="margin-top: 10px; width: 100%;"
        ),
        Button(
            "Coupon", 
            type="button", 
            onclick="showContent('coupon')",
            style="margin-top: 10px; width: 100%;"
        ),
        style="display: flex; flex-direction: column; gap: 10px; width: 250px; padding: 10px; border-right: solid 1px #ccc; height: 100vh; background-color: #121212;"
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
                        onclick="document.getElementById('fileInput').click();",
                        style="margin-top: 10px;"
                    ),
                    style="display: flex; gap: 10px; align-items: center;"
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
                    action="/update_username",
                    style="display: flex; flex-direction: column; gap: 5px; align-items: center; margin-top: 10px;"
                ),
                Input(
                    type="file",
                    id="fileInput",
                    onchange="updateProfileImage(event)",
                    style="display: none;"
                ),
                style="border: solid; padding: 20px; display: flex; flex-direction: column; align-items: center; gap: 10px; background-color: #121212;"
            ),
            id="profileContent",
            style="display: block;"
        ),
        
        Div(
            Div(
                *[
                    Div(
                        Div(f"District: {address.district}", id=f"district_{address.district}", style="margin-top: 10px; padding: 5px;"),
                        Div(f"Province: {address.province}", id=f"province_{address.province}", style="margin-top: 10px; padding: 5px;"),
                        Div(f"Zip Code: {address.zip_code}", id=f"zip_{address.zip_code}", style="margin-top: 10px; padding: 5px;"),
                        Div(f"Phone Number: {address.phone_number}", id=f"phone_{address.phone_number}", style="margin-top: 10px; padding: 5px;"),
                        
                        Button(
                            "Edit",
                            type="button",
                            onclick=f"toggleEditAddress('{address.district}')",
                            style="margin-top: 10px;"
                        ),
                        
                        Div(
                            Input(type="text", id=f"editDistrict_{address.district}", value=address.district, style="display: none; margin-top: 10px;"),
                            Input(type="text", id=f"editProvince_{address.province}", value=address.province, style="display: none; margin-top: 10px;"),
                            Input(type="text", id=f"editZip_{address.zip_code}", value=address.zip_code, style="display: none; margin-top: 10px;"),
                            Input(type="text", id=f"editPhone_{address.phone_number}", value=address.phone_number, style="display: none; margin-top: 10px;"),
                            Button(
                                "Save",
                                type="button",
                                onclick=f"saveAddress('{address.district}')",
                                style="display: none; margin-top: 10px;"
                            ),
                            style="display: none; flex-direction: column;"
                        ),
                        style="margin-top: 10px; padding: 10px; border: 1px solid #ccc; background-color: #fff; color: #121212; border-radius: 5px; width: 300px;"  # Adjusted width for the cards
                    ) for address in sorted(address_list, key=lambda x: x.district)  # Sorting by district (you can adjust this to another field if needed)
                ],
                id="addressContent",
                style="display: flex; flex-direction: row; gap: 20px; margin-top: 20px; flex-wrap: wrap;"  # Ensure cards wrap in a row
            ),
        ),
        
        Div(
            "Transaction history...",
            id="transactionContent",
            style="display: none;"
        ),
        
        Div(
            "Coupons used...",
            id="couponContent",
            style="display: none;"
        ),
        style="flex-grow: 1; padding: 20px; background-color: #121212;" 
    )

    main_content = Div(
        left_menu,
        content_area,
        style="display: flex; height: 100vh; background-color: #121212;"
    )

    script = Script("""
        function showContent(contentType) {
         document.getElementById('profileContent').style.display = 'none';
          document.getElementById('transactionContent').style.display = 'none';
         document.getElementById('couponContent').style.display = 'none';
        document.getElementById('addressContent').style.display = 'none';

         if (contentType === 'profile') {
        document.getElementById('profileContent').style.display = 'block';
        document.getElementById('addressContent').style.display = 'flex';  // Ensure addressContent is displayed
        document.getElementById('addressContent').style.flexDirection = 'row';  // Set address cards to horizontal layout
         } else if (contentType === 'transaction') {
        document.getElementById('transactionContent').style.display = 'block';
         } else if (contentType === 'coupon') {
        document.getElementById('couponContent').style.display = 'block';
        }
        }


        function toggleEditAddress(district) {
            document.getElementById('editDistrict_' + district).style.display = 'block';
            document.getElementById('editProvince_' + district).style.display = 'block';
            document.getElementById('editZip_' + district).style.display = 'block';
            document.getElementById('editPhone_' + district).style.display = 'block';
            document.getElementById('saveAddress_' + district).style.display = 'block';
        }

        function saveAddress(district) {
            var updatedDistrict = document.getElementById('editDistrict_' + district).value;
            var updatedProvince = document.getElementById('editProvince_' + district).value;
            var updatedZip = document.getElementById('editZip_' + district).value;
            var updatedPhone = document.getElementById('editPhone_' + district).value;

            document.getElementById('editDistrict_' + district).style.display = 'none';
            document.getElementById('editProvince_' + district).style.display = 'none';
            document.getElementById('editZip_' + district).style.display = 'none';
            document.getElementById('editPhone_' + district).style.display = 'none';
            document.getElementById('saveAddress_' + district).style.display = 'none';

            document.getElementById('district_' + district).innerText = 'District: ' + updatedDistrict;
            document.getElementById('province_' + district).innerText = 'Province: ' + updatedProvince;
            document.getElementById('zip_' + district).innerText = 'Zip Code: ' + updatedZip;
            document.getElementById('phone_' + district).innerText = 'Phone Number: ' + updatedPhone;
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

        function updateProfileImage(event) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('profileImage').src = e.target.result;
            }
            reader.readAsDataURL(event.target.files[0]);
        }
    """)

    page = Main(
        part_header,
        main_content,
        script,
        style=Component.configHeader
    )
    
    return page
