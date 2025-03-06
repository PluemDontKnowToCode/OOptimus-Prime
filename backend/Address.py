#region Address
class Address:
    #district = เขต
    #province  = ตำบล
    #zipcode = ไปรษณีย์
    def __init__(self, district = "", province="", zip_code="", phone_number=""):
        self.__district = district
        self.__province = province
        self.__zip_code = zip_code
        self.__phone_number = phone_number

    def to_json(self):
        return {
            "district" : self.__district,
            "province" : self.__province,
            "zip_code" : self.__zip_code,
            "phone" : self.__phone_number
        }
    
    @property
    def district(self):
        return self.__district
    
    @property
    def province(self):
        return self.__province
    
    @property
    def zip_code(self):
        return self.__zip_code
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    def is_equal(self, address):
        if(address == None):
            return False
        if(self.district != address.district):
            return False
        if(self.province != address.province):
            return False
        if(self.zip_code != address.zip_code):
            return False
        if(self.phone_number != address.phone_number):
            return False
        return True
#endregion