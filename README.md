# OOptimus-Prime
OOP project

## Getting Started

To run this project locally, ensure you have Python installed. Then, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PluemDontKnowToCode/OOptimus-Prime.git
   ```
2. **Set Up Project**:
   ```bash
   cd OOptimus-Prime
   pip install -r requirements.txt
   ```
3. **Run Project**
   ```bash
   cd OOptimus-Prime
   python -u ./_main.py
   ```
   or run ***run.bat*** in **OOptimus-Prime/frontend/run.bat** to start then go to **localhost:3000**

4. **Data File**

   this project didn't connect to any backend so all data come from following json file
   ## Data File Structure
   
   The following structure represents the organization of JSON data files:
   ```bash
   jsonData
   
      │── Account.json
   
      │── Admin.json
   
      │── Coupon.json
   
      │── Product.json
   
      │── Seller.json
   
      │── UnImproveProduct.json
      ```
   **Note admin username must have "admin" in it**
## Features

- **User Authentication**: Users can register, log in, and log out.
- **Profile Management**: Users can update their profile information, including username and profile image.
- **Product Management**: Sellers can add new products, and admins can approve or reject product requests.
- **Shopping Cart**: Customers can add products to their cart, view cart details, and proceed to checkout.
- **Coupon Management**: Admins can create and delete coupons, and customers can apply coupons during checkout.
- **Address Management**: Customers can add, update, and delete addresses.
- **Transaction History**: Customers can view their transaction history.
- **Category Browsing**: Users can browse products by categories.
- **Responsive Design**: The application is designed to be responsive and user-friendly.
