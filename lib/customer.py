class Customer:
    def __init__(self, username, name, phone_number):
        self.username = username
        self.name = name
        self.phone_number = phone_number
        self.visit_number = 0
    
    def view_username(self):
        return self.username
    
    def view_name(self):
        return self.name
    
    def view_phone_number(self):
        return self.phone_number
    
    def update_username(self, username):
        self.username = username
        return f'Your username has been changed to {username}'
    
    def update_name(self, name):
        self.name = name
        return f'Your name has been changed to {name}'
    
    def update_phone_number(self, phone_number):
        self.phone_number = phone_number
        return f'Your phone number has been changed to {phone_number}'