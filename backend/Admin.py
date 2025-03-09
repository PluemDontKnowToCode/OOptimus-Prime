from backend.Account import *
from backend.RequestedProduct import *

class Admin(Account):
    def __init__():
        super().__init__(id)

    def __init__(self, d: dict, market = None):
        super().__init__(d, market)

    def approve_product(self, request):
        if(isinstance(request, RequestedProduct)):
            request.update_status("Approve")
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