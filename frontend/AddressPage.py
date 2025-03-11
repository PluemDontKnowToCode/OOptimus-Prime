from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page():
    role_bool = isinstance(market1.current_account, Customer)
    current_account = market1.current_account
    address_list = current_account.address_list if role_bool else []

    part_header = Component.Header(False)

    # Add the "X" button to navigate back to the profile page
    back_button = Button(
        "X",
        type="button",
        onclick="window.location.href = '/profile'",
        style="position: absolute; top: 30px; right: 30px; background-color: red; color: white; border: none; padding: 30px; border-radius: 50%; cursor: pointer;"
    )

    # Form for adding new addresses
    add_address_form = Form(
        Div(
            Input(type="text", name="district", placeholder="District", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="province", placeholder="Province", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="zip_code", placeholder="Zip Code", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="phone_number", placeholder="Phone Number", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Button("Add Address", type="submit", style="margin-top: 10px; padding: 10px; background-color: green; color: white; border: none; cursor: pointer;"),
            style="display: flex; flex-direction: column; gap: 10px; width: 300px; padding: 10px; border: 1px solid #ccc; background-color: #fff; color: #121212; border-radius: 5px;"
        ),
        method="post",
        action="/address/add",
        onsubmit="return validateAddressForm()"
    )

    address_content = Div(
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
                Button(
                    "Delete",
                    type="button",
                    onclick=f"deleteAddress('{address.district}')",
                    style="margin-top: 10px; background-color: red; color: white; border: none; cursor: pointer;"
                ),
                
                Div(
                    Input(type="text",
                        id=f"editDistrict_{address.district}",
                        value=address.district,
                        onclick="toggleEditAddress{address.district}", 
                        style="display: none; margin-top: 10px;"),
                    Input(type="text",
                        id=f"editProvince_{address.province}",
                        value=address.province,
                        onclick= "toggleEditAddress{address.province}", 
                        style="display: none; margin-top: 10px;"),
                    Input(type="text",
                        id=f"editZip_{address.zip_code}",
                        value=address.zip_code,
                        onclick="toggleEditAddress{address.zip_code}" , 
                        style="display: none; margin-top: 10px;"),
                    Input(type="text",
                        id=f"editPhone_{address.phone_number}",
                        value=address.phone_number,
                        onclick= "toggleEditAddress{address.phone_number}", 
                        style="display: none; margin-top: 10px;"),
                    Button(
                        "Save",
                        type="button",
                        id=f"saveAddressButton_{address.district}",
                        onclick=f"saveAddress(event, '{address.district}')",
                        style="display: none; margin-top: 10px;"
                    ),
                    Button(
                        "Cancel",
                        type="button",
                        onclick=f"cancelEditAddress('{address.district}')",
                        style="display: none; margin-top: 10px;"
                    ),
                    style="display: none; flex-direction: column; gap: 10px;"
                ),
                style="margin-top: 10px; padding: 10px; border: 1px solid #ccc; background-color: #fff; color: #121212; border-radius: 5px; width: 300px;"  # Adjusted width for the cards
            ) for address in sorted(address_list, key=lambda x: x.district)  # Sorting by district (you can adjust this to another field if needed)
        ],
        id="addressContent",
        style="display: flex; flex-direction: row; gap: 20px; margin-top: 20px; flex-wrap: wrap;"  # Ensure cards wrap in a row
    ) if role_bool else Div()

    main_content = Div(
        back_button,  # Add the back button to the main content
        add_address_form,  # Add the form for adding new addresses
        address_content,
        style="flex-grow: 1; padding: 20px; background-color: #121212; position: relative;"
    )

    script = ("""
        function toggleEditAddress(district) {
            document.getElementById('editDistrict_' + district).style.display = 'block';
            document.getElementById('editProvince_' + district).style.display = 'block';
            document.getElementById('editZip_' + district).style.display = 'block';
            document.getElementById('editPhone_' + district).style.display = 'block';
            document.getElementById('saveAddressButton_' + district).style.display = 'block';
            document.getElementById('cancelAddress_' + district).style.display = 'block';

            document.getElementById('district_' + district).style.display = 'none';
            document.getElementById('province_' + district).style.display = 'none';
            document.getElementById('zip_' + district).style.display = 'none';
            document.getElementById('phone_' + district).style.display = 'none';
        }

        function saveAddress(event, old_district) {
            event.preventDefault(); // Prevent page refresh

            var updatedDistrict = document.getElementById('editDistrict_' + old_district).value;
            var updatedProvince = document.getElementById('editProvince_' + old_district).value;
            var updatedZip = document.getElementById('editZip_' + old_district).value;
            var updatedPhone = document.getElementById('editPhone_' + old_district).value;

            fetch('/address/update', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    old_district: old_district,
                    new_district: updatedDistrict,
                    new_province: updatedProvince,
                    new_zip_code: updatedZip,
                    new_phone_number: updatedPhone
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('editDistrict_' + old_district).style.display = 'none';
                    document.getElementById('editProvince_' + old_district).style.display = 'none';
                    document.getElementById('editZip_' + old_district).style.display = 'none';
                    document.getElementById('editPhone_' + old_district).style.display = 'none';
                    document.getElementById('saveAddressButton_' + old_district).style.display = 'none';
                    document.getElementById('cancelAddress_' + old_district).style.display = 'none';

                    document.getElementById('district_' + old_district).innerText = 'District: ' + updatedDistrict;
                    document.getElementById('province_' + old_district).innerText = 'Province: ' + updatedProvince;
                    document.getElementById('zip_' + old_district).innerText = 'Zip Code: ' + updatedZip;
                    document.getElementById('phone_' + old_district).innerText = 'Phone Number: ' + updatedPhone;

                    document.getElementById('district_' + old_district).style.display = 'block';
                    document.getElementById('province_' + old_district).style.display = 'block';
                    document.getElementById('zip_' + old_district).style.display = 'block';
                    document.getElementById('phone_' + old_district).style.display = 'block';
                } else {
                    alert('Failed to update address.');
                }
            })
            .catch(error => console.error('Error:', error));
        }

        function cancelEditAddress(district) {
            document.getElementById('editDistrict_' + district).style.display = 'none';
            document.getElementById('editProvince_' + district).style.display = 'none';
            document.getElementById('editZip_' + district).style.display = 'none';
            document.getElementById('editPhone_' + district).style.display = 'none';
            document.getElementById('saveAddressButton_' + district).style.display = 'none';
            document.getElementById('cancelAddress_' + district).style.display = 'none';

            document.getElementById('district_' + district).style.display = 'block';
            document.getElementById('province_' + district).style.display = 'block';
            document.getElementById('zip_' + district).style.display = 'block';
            document.getElementById('phone_' + district).style.display = 'block';
        }

        function deleteAddress(district) {
            fetch('/address/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ district: district })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Address deleted successfully!');
                    window.location.reload();
                } else {
                    alert('Failed to delete address.');
                }
            })
            .catch(error => console.error('Error:', error));
        }

        function validateAddressForm() {
            var district = document.querySelector('input[name="district"]').value;
            var province = document.querySelector('input[name="province"]').value;
            var zip_code = document.querySelector('input[name="zip_code"]').value;
            var phone_number = document.querySelector('input[name="phone_number"]').value;

            if (!district || !province || !zip_code || !phone_number) {
                alert('All fields are required.');
                return false;
            }

            return true;
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
