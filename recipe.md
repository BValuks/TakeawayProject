1. Describe the Problem
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as Thank you! Your order was placed and will be delivered before 18:52 after I have ordered.

                                            PERSONAL ORGANISER



               ┌─────────────────────────┐
               │ Menu                    │
               │                         │
               │ -init (Nested dict)     │
               │                         │▲─────────────────────────────┬───┐
               │                         ├──────────────────────────────┤   │
               └───────────────────┬─────┘                              │   │
                                   │    ▲                               │   │
                                   │    │                               │   │
                                   │    │                               │   │
                                   │    │                               │   │
                                   │    │                               │   │
                                   ▼    │                               ▼   │
   ┌────────────┐              ┌────────┴───────────┐               ┌───────┴─┐
   │            │              │                    │               │         │
   │ TextSender │ ◄────────────┤   Order            │               │ Receipt │
   │            │              │                    ├─────────────► │         │
   └────────────┘              │-init (Receipt)     │               └─────────┘
         ▲                     │      (Customer)    │
         │                     │      (TextSender)  │
         │                     │-view_menu          │◄───────────┐
         │                     │-place_order        │            │
         │                     │    -send text      │            │
         │                     │-view_receipt       │            │    Nouns                 Verbs
         │                     │                    │            │
         │                     │                    │            │    *Customer             *Check
         │                     │                    │            │    *List                 *Order
         │                     │                    │            │    *Dishes               *View
         │                     │                    │            │    *Prices               *Select
         │                     └───┬────────────────┘            │    *Meal                 *Verify
         │                         │        ▲                    │    *Order                *Receive
         │                         │        │                    │    *Receipt
         │                         │        │                    │    *Grand total
         │                         │        │                    │    *Text message
         │                         │        │                    │
         │                         │        │                    │
         │                         ▼        │                    │
         │                    ┌─────────────┴───────┐            │
         │                    │                     │       ┌────┴─────────┐
         │                    │ Customer            │       │ CustomerList │
         └────────────────────┤                     ├─────► │              │
                              │-init (name, number) │       └──────────────┘
                              │                     │
                              └─────────────────────┘












Also design the interface of each class in more detail.

class Menu:

    def __init__(self):
        # self.menu_items: A nested dictionary of all menu items, sorted by type e.g. starter, main etc
        # self.items_sold: A list of dictionaries with all the items sold and the number of each sold
    
    def view_items_sold(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of dictionaries containing the items and amounts of items sold
        # Side-effects:
        #   None
        pass # No code here yet

    def reset_items_sold(self):
        # Parameters:
        #   None
        # Returns:
        #   A string stating that the items sold list has been reset
        # Side-effects:
        #   Assigns an empty list to self.items_sold
        pass # No code here yet

class Order:

    def __init__(self, menu):
        # menu: An instance of the menu class
        # self.basket: A list containing all the menu items that have been added 
        # self.receipt: An instance of the receipt class
        # self.customer: Has default value of None but if repeat customer, can enter customer name. Otherwise one will be assigned at place_order.
        # self.text_sender: An instance of the TextSender class

    def view_menu(self):
        # Parameters:
        #   None
        # Returns:
        #   A nested dictionary of menu items split by type e.g. starter, main
        # Side-effects:
        #   None
        pass # No code here yet

    def view_popular_items(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted string with the top 3 items that have sold the most
        # Side-effects:
        #   None
        pass # No code here yet

    def add_to_basket(self, item):
        # Parameters:
        #   item: A string representing a menu item
        # Returns:
        #   A string saying the item has been added to the basket
        # Side-effects:
        #   Reduces the stock figure for the item selected
        pass # No code here yet

    def view_basket(self):
        # Parameters:
        #   None
        # Returns:
        #   A string containing the items in the basket and the number of each item
        # Side-effects:
        #   None
        pass # No code here yet

    def remove_from_basket(self, item):
        # Parameters:
        #   item: A string representing an item in the basket
        # Returns:
        #   A string saying the item has been removed from the basket
        # Side-effects:
        #   Adds to the stock figure for the given menu item
        pass # No code here yet

    def place_order(self):
        # Parameters:
        #   None
        # Returns:
        #   1st iteration - A string saying the user must use new_customer() or customer_login before placing order
        #   2nd iteration - A formatted string thanking them for their order and informing them that they should receive a confirmation text soon
        # Side-effects:
        #   Calls the instance of the TextSender class to send a confirmation text to the user
        #   Adds items to the items_sold list attached to the Menu class
        pass # No code here yet

    def new_customer(self, username, name, phone_number):
        # Parameters:
        #   username: A string representing a unique username
        #   name: A string representing the customer's name
        #   phone_number: an integer representing the customer's phone number
        # Returns:
        #   A string welcoming the user as a new customer
        # Side-effects:
        #   Adds the customer to the CustomerList
        pass # No code here yet

    def customer_login(self, username):
        # Parameters:
        #   customer: An instance of the customer class
        # Returns:
        #   A string welcoming welcoming the customer back
        # Side-effects:
        #   Assigns the customer to self.customer
        pass # No code here yet

    def view_itemised_receipt(self):
        # Parameters:
        #   None
        # Returns:
        #   A string with the number and price of each item with a total at the bottom
        # Side-effects:
        #   None
        pass # No code here yet

class Customer:

    def __init__(self, username, name, phone_number):
        # self.username: A string representing the customers username
        # self.name: A string representing the customers name
        # self.phone_number: An string representing the customers phone number
        # self.visit_number: An integer representing the number of times the customer has visited the takeaway

    def number_of_visits(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted string with the visitor name and the number of visits
        # Side-effects:
        #   None
        pass # No code here yet

    def view_username(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted string representing the value of self.userWname
        # Side-effects:
        #   None
        pass # No code here yet

    def view_name(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted string representing the value of self.name
        # Side-effects:
        #   None
        pass # No code here yet

    def view_phone_number(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted string representing the value of self.phone_number
        # Side-effects:
        #   None
        pass # No code here yet

    def update_username(self, username):
        # Parameters:
        #   username: A string representing the new username to be assigned to the customer
        # Returns:
        #   A string saying the username has been changed, referencing both AS LONG AS the username is unique
        # Side-effects:
        #   Changes the value of self.username
        pass # No code here yet

    def update_name(self, name):
        # Parameters:
        #   name: A string representing the new name to be assigned to the customer
        # Returns:
        #   A string saying the name has been changed, referencing both
        # Side-effects:
        #   Changes the value of self.name
        pass # No code here yet

    def update_phone_number(self, phone_number):
        # Parameters:
        #   phone_number: An integer representing the new phone number to be assigned to the customer
        # Returns:
        #   A string saying the phone number has been changed, referencing the new number
        # Side-effects:
        #   Changes the value of self.name
        pass # No code here yet

class CustomerList:

    def __init__(self):
        # self.customer_list: A dictionary with keys being the name of the customer and values being a dictionary of phone numbers and visit numbers 

    def view_customers(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the names of all the customers
        # Side-effects:
        #   None
        pass # No code here yet

    def view_customer_by_username(self, name):
        # Parameters:
        #   name: A string representing a customer name
        # Returns:
        #   A formatted string with the customer information
        # Side-effects:
        #   None
        pass # No code here yet

    def view_top_customers(self, number):
        # Parameters:
        #   number: An integer representing the number of top customers we want to see e.g. top 3, top 5, top 10 etc
        # Returns:
        #   A formatted string with the top visitor names and the number of visits
        # Side-effects:
        #   None
        pass # No code here yet

    def add_customer(self, username name, phone_number):
        # Parameters:
        #   username: A string representing a unique username
        #   name: A string representing the customer's name
        #   phone_number: A string representing the customer's phone number
        # Returns:
        #   A string stating that the customer has been added
        # Side-effects:
        #   Adds the customer to self.customer_list
        pass # No code here yet

    def remove_customer(self, name):
        # Parameters:
        #   name: A string representing the customer's name
        # Returns:
        #   A string stating that the customer has been removed
        # Side-effects:
        #   Removes the customer to self.customer_list
        pass # No code here yet

class Receipt:

    def __init__(self):
        # None

    def get_receipt(self):
        # Parameters:
        #   None
        # Returns:
        #   A string with the number and price of each item with a total at the bottom
        # Side-effects:
        #   None
        pass # No code here yet


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given an instance of Order
We can view the menu
"""
menu = Menu()
order1 = Order(menu)
order1.view_menu() # => {menu_items}

"""
Given an instance of Order
We can add an item and view it in the basket
"""
menu = Menu()
order1 = Order(menu)
order1.add_to_basket('Cheeseburger') # => 'Cheeseburger has been added to your basket'
order1.view_basket() # => 'The following items are in your basket: 1 x Cheeseburger'
order1.add_to_basket('Onion Rings') # => 'Onion Rings has been added to your basket'
order1.add_to_basket('Cheeseburger') # => 'Cheeseburger has been added to your basket'
order1.view_basket() # => 'The following items are in your basket: 2 x Cheeseburger, 1 x Onion Rings'

"""
Given an instance of Order
We can add an item to the basket and see that the available stock has decreased when we view menu
"""
menu = Menu()
order1 = Order(menu)
order1.view_menu() # => {'Cheeseburger': {'Price': 10.00, 'Stock': 5}}
order1.add_to_basket('Cheeseburger')
order1.view_menu() # => {'Cheeseburger': {'Price': 10.00, 'Stock': 4}}

"""
Given an instance of Order
We try and add an item with a stock count of zero and it raises an exception
"""
menu = Menu()
order1 = Order(menu)
order1.view_menu() # => {'Pulled Pork Burger': {'Price': 12.00, 'Stock': 0}}
order1.add_to_basket('Pulled Pork Burger') # => 'Item out of stock.'

"""
Given an instance of Order
We can remove an item from the basket and the stock count increases to reflect this
"""
menu = Menu()
order1 = Order(menu)
order1.view_menu() # => {'Cheeseburger': {'Price': 10.00, 'Stock': 5}}
order1.add_to_basket('Cheeseburger')
order1.view_menu() # => {'Cheeseburger': {'Price': 10.00, 'Stock': 4}}
order.view_basket() # => 'The following items are in your basket: 1 x Cheeseburger'
order.remove_from_basket('Cheeseburger') # => 'Cheeseburger has been removed from your basket'
order.view_basket() # => 'You have no items in your basket'
order1.view_menu() # => {'Cheeseburger': {'Price': 10.00, 'Stock': 5}}

"""
Given an instance of Order
If we try to remove an item that isn't in the basket, it throws and error
"""
menu = Menu()
order = Order(menu)
order.add_to_basket('Onion Rings')
order.remove_from_basket('Cheeseburger') # => 'The item is not in your basket'

"""
Given an instance of Order
If we try to remove an item if the basket is empty, it throws an error
"""
menu = Menu()
order = Order(menu)
order.remove_from_basket('Cheeseburger') # => 'Basket is empty'

"""
Given an instance of Order
We can view an itemised receipt
"""
menu = Menu()
order1 = Order(menu)
order1.add_to_basket('Cheeseburger')
order1.add_to_basket('Onion Rings')
order1.add_to_basket('Cheeseburger')
order1.view_itemised_receipt() # => 'Your order: 2 x Cheesburger £20, 1 x Onion Rings £6 | Total: £26'

"""
Given an instance of Order
We place an order and we're told to login or set up a new customer
"""
menu = Menu()
order1 = Order(menu)
order1.add_to_basket('Cheeseburger')
order1.place_order() # => 'Please use either customer_login or new_customer.'

"""
Given an instance of CustomerList
We can add some customers and view them as a list and by searching by customer and then remove a customer
"""
customer_list = CustomerList()
customer_list.add_customer('BVal', 'Benedict', '07965430788') # => 'Benedict has been added as a customer'
customer_list.add_customer('LizA' 'Lizzie', '02084536661') # => 'Lizzie has been added as a customer'
customer_list.view_customers() # => ['BVal', 'LizA']
customer_list.view_customer_by_username('LizA') # => 'Username: LizA, Name: Lizzie, Phone number: 02084536661, Number of visits: 0'
customer_list.remove_customer('BVal') # => 'Benedict (BVal) has been removed from the customer list.'
customer_list.view_customers() # => ['LizA']

"""
Given an instance of Order
We place an order with a customer supplied with #new_customer
"""
menu = Menu()
customer_list = CustomerList()
order1 = Order(menu)
order1.add_to_basket('Cheeseburger')
order1.new_customer('BenV', 'Benedict', '07965430788')
order1.place_order() # => 'Thank you for your order Benedict. You should receive text confirmation soon.'

"""
Given an instance of Order
We place an order with a customer supplied with #customer_login
"""
menu = Menu()
customer_list = CustomerList()
customer_list.add_customer('BenV', 'Benedict', '07965430788') # => 'Benedict (BenV) has been added as a customer'
order1 = Order(menu)
order1.add_to_basket('Cheeseburger')
order1.customer_login('BenV')
order1.place_order() # => 'Thank you for your order Benedict. You should receive text confirmation soon.'

"""
Given an instance of CustomerList
We can call #view_top_customers and see the top customers by number of visits and see popular dishes
"""
menu = Menu()
customer_list = CustomerList()
customer_list.add_customer('BenV' 'Benedict', '07965430788')
customer_list.add_customer('LizA', 'Lizzie', '02084536661')
customer_list.add_customer('NoahV', 'Noah', '07264009867')
customer_list.add_customer('Simyarn', 'Simeon', '07839104213')

order_benedict1 = Order(menu)
order_lizzie1 = Order(menu)
order_noah1 = Order(menu)
order_simeon1 = Order(menu)

order_benedict1.add_to_basket('Cheeseburger')
order_benedict1.customer_login('BVal')
order_benedict1.place_order()

order_benedict2 = Order(menu)
order_benedict2.add_to_basket('Cheeseburger')
order_benedict2.customer_login('BVal')
order_benedict2.place_order()

order_lizzie1.add_to_basket('Onion Rings')
order_lizzie1.customer_login('LizA')
order_lizzie1.place_order()

order_noah1.add_to_basket('Coke')
order_noah1.customer_login('NoahV')
order_noah1.place_order()

order_noah2 = Order(menu)
order_noah2.add_to_basket('Coke')
order_noah2.customer_login('NoahV')
order_noah2.place_order()

order_noah2 = Order(menu)
order_noah3.add_to_basket('Coke')
order_noah3.customer_login('NoahV')
order_noah3.place_order()

order_noah4 = Order(menu)
order_noah4.add_to_basket('Coke')
order_noah4.customer_login('NoahV')
order_noah4.place_order()

order_simeon1.add_to_basket('Chicken Burger')
order_simeon1.customer_login('Simyarn')
order_simeon1.place_order()

order_simeon2 = Order(menu)
order_simeon2.add_to_basket('Chicken Burger')
order_simeon2.customer_login('Simyarn')
order_simeon2.place_order()

order_simeon3 = Order(menu)
order_simeon3.add_to_basket('Chicken Burger')
order_simeon3.customer_login('Simyarn')
order_simeon3.place_order()

customer_list.view_top_customers(2) # => 'Top customers| Noah (NoahV) - No. of visits: 4, Simeon (Simyarn) - No. of visits: 3' 
customer_list.view_top_customers(3) # => 'Top customers| Noah (NoahV) - No. of visits: 4, Simeon (Simyarn) - No. of visits: 3, Benedict (BenV) - No. of visits: 2' 
customer_list.view_top_customers(4) # => 'Top customers| Noah (NoahV) - No. of visits: 4, Simeon (Simyarn) - No. of visits: 3, Benedict (BenV) - No. of visits: 2, Lizzie (LizA) - No. of visits: 1'

order1 = Order(menu)
order1.view_popular_items() # => 'Top items: 1. Coke, 2. Chicken Burger, 3. Cheeseburger'

"""
Given an instance of CustomerList
Attempting to add a new customer with a username that is not unique throws an error
"""
customer_list = CustomerList()
customer_list.add_customer('BenV' 'Benedict', '07965430788')
customer_list.add_customer('LizA', 'Lizzie', '02084536661')
customer_list.add_customer('BenV' 'Benjamin', '01805787254') # => 'Username already in use. Please choose another.'

"""
Given an instance of Menu
We can use #view_items_sold to view items and amount of items sold and use #reset_items_sold to reset the items sold list
"""
menu = Menu()
order = Order(menu)
order.add_to_basket('Cheeseburger')
order.add_to_basket('Onion Rings')
order.add_to_basket('Cheeseburger')
menu.view_items_sold() # => [{'Cheeseburger: 2}, {'Onion Rings': 1}]
menu.reset_items_sold()
menu.view_items_sold() # => []

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

--------------------------------------MENU
"""
Given an instance of Menu
We view view items sold and then reset the list
"""
menu = Mock()
menu.items_sold.return_value = [{'Cheeseburger: 2}, {'Onion Rings': 1}]
menu.view_items_sold() # => [{'Cheeseburger: 2}, {'Onion Rings': 1}]
menu.reset_items_sold()
menu.view_items_sold() # => []

--------------------------------------CUSTOMER

"""
Given an instance of Customer
We can use #view_username, #view_name, #view_phone_number to view those variables 
"""
customer = Customer('BVal', 'Benedict', '07123456789')
customer.view_username() # => 'BVal'
customer.view_name() # => 'Benedict'
customer.view_phone_number() # => '07123456789'

"""
Given an instance of Customer
We can use #update_username, #update_name, #update_phone_number to update those variables 
"""
customer = Customer('BVal', 'Benedict', '07123456789')
customer.update_username('LizA') # => 'Your username has been changed to LizA'
customer.update_name('Lizzie') # => 'Your name has been changed to Lizzie'
customer.update_phone_number('07987654321') # => 'Your phone number has been changed to 07987654321'
customer.view_username() # => 'LizA'
customer.view_name() # => 'Lizzie'
customer.view_phone_number() # => '07987654321'




5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.