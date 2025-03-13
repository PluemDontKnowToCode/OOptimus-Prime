from fasthtml.common import *
import Component
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.lib255 import *

def page():
    role_bool = isinstance(market1.current_user, Customer)
    current_user = market1.current_user
    address_list = current_user.address_list if role_bool else []

    part_header = Component.Header(False)

    back_button = Button(
        "Back",
        type="button",
        onclick="window.location.href = '/profile'",
        style="position: absolute; top: 10px; right: 20px; background-color: blue; color: white; border: none; padding: 20px; border-radius: 20px; cursor: pointer;"
    )

    add_address_form = Form(
        Div(
            Input(type="text", name="district", placeholder="District", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="province", placeholder="Province", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="zip_code", placeholder="Zip Code", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Input(type="text", name="phone_number", placeholder="Phone Number", style="margin-top: 10px; padding: 5px; width: 100%;"),
            Button("Add Address", type="submit", style="margin-top: 10px; padding: 10px; background-color: green; color: white; border: none; cursor: pointer;"),
            style="display: flex; flex-direction: column; gap: 10px; width: 300px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;"
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
                    "Delete",
                    type="button",
                    onclick=f"deleteAddress('{address.district}')",
                    style="margin-top: 10px; background-color: red; color: white; border: none; cursor: pointer;"
                ),
                
                
                style="margin-top: 10px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 300px;"  # Adjusted width for the cards
            ) for address in sorted(address_list, key=lambda x: x.district)  
        ],
        id="addressContent",
        style="display: flex; flex-direction: row; gap: 20px; margin-top: 20px; flex-wrap: wrap;"
    ) if role_bool else Div()

    main_content = Div(
        back_button,
        add_address_form,
        address_content,
        style="flex-grow: 1; padding: 20px; position: relative;"
    )

    script = ("""
        

        function deleteAddress(district) {
            console.log('Attempting to delete address:', district); // Debug log

            fetch('/address/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ district: district })
            })
            .then(response => {
                console.log('Response received:', response); // Debug log
                return response.json();
            })
            .then(data => {
                console.log('Data received:', data); // Debug log
                if (data.success) {
                    alert('Address deleted successfully!');
                    window.location.reload();
                } else {
                    alert('Failed to delete address.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while deleting the address.');
            });
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

