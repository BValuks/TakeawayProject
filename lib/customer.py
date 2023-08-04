class Customer:
    def __init__(self, username, name, phone_number):
        self.username = username
        self.name = name
        self.phone_number = phone_number
    
    def view_username(self):
        return self.username
    
    def view_name(self):
        return self.name
    
    def view_phone_number(self):
        return self.phone_number