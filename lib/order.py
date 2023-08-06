# from menu import Menu
# from basket import Basket
# from receipt import Receipt
# from customer import Customer
# from customer_list import CustomerList
from lib.basket import Basket
from lib.receipt import Receipt
from lib.customer import Customer
from lib.customer_list import CustomerList

class Order:
    def __init__(self, menu, customer_list):
        self.menu = menu
        self.customer_list = customer_list
        self.basket = Basket(menu) # example: {'Cheeseburger': 1}
        self.receipt = Receipt(menu, self.basket)
        self.customer = None

    def view_menu(self):
        return self.menu.formatted_menu()
    
    def view_popular_items(self):
        return self.menu.popular_items()
    
    def add_to_basket(self, item):
        return self.basket.add_to_basket(item)
    
    def remove_from_basket(self, item):
        return self.basket.remove_from_basket(item)

    def view_basket(self):
        return self.basket.view_basket()
    
    def empty_basket(self):
        return self.basket.empty_basket()
    
    def view_itemised_receipt(self):
        return self.receipt.get_receipt()
    
    def place_order(self):
        if self.customer == None:
            return 'Please use either customer_login or new_customer.'
        else:
            self.customer.visit_number += 1
            self.basket.items_ordered()
            self.basket = Basket(self.menu)
            return f'Thank you for your order {self.customer.name}. You should receive text confirmation soon.'
    
    def new_customer(self, username, name, phone_number):
        self.customer = Customer(username, name, phone_number)
        self.customer_list.add_customer(username, name, phone_number)
        return f'Welcome to the team {name}, we hope you enjoy your food'
    
    def customer_login(self, username):
        name = None
        for customer in self.customer_list.customer_list:
            if customer.username == username:
                self.customer = customer
                name = customer.name
        return f'Welcome back {name}'

# menu = Menu()
# order = Order(menu)
# order.add_to_basket('Cheeseburger')
# order.add_to_basket('Cheeseburger')
# order.remove_from_basket('Cheeseburger')
# order.add_to_basket('Cheeseburger')
