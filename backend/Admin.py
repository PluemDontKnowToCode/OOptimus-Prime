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

    def rejected_product(self, request):
        if(isinstance(request, RequestedProduct)):
            request.update_status("Reject")