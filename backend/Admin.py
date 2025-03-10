from backend.Account import *
from backend.RequestedProduct import *
from datetime import datetime, timedelta
from backend.Coupon import *

class Admin(Account):
    def __init__():
        super().__init__(id)

    def __init__(self, d: dict, market = None):
        super().__init__(d, market)

    def create_coupon(self, discount_percent, less_amount, product_count, duration):
        new_date = datetime.now() + timedelta(days=duration)

        # Convert to string format "YYYY-MM-DD"
        coupon = Coupon(super().market.generate_id(4),discount_percent, less_amount, product_count, datetime.now(),new_date)
        self.market.add_coupon(coupon)
        return "Create Success"
    
    def delete_coupon(self, id):
        return self.market.delete_coupon(id)

    def approve_product(self, request):
        if(isinstance(request, RequestedProduct)):
            request.update_status("Approve")
            request.seller.add
            super().market.add_product(request.product)

    def reject_product(self, request):
        if(isinstance(request, RequestedProduct)):
            request.update_status("Reject")

    def get_requested_product(self):
        res = []
        requested = super().market.requested_list
        for i in requested:
            if i.status == "Idle":
                res.append(i)
        return res