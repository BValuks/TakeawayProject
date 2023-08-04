# from menu import Menu
from lib.basket import Basket
from lib.receipt import Receipt

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.basket = Basket(menu) # example: {'Cheeseburger': 1}
        self.receipt = Receipt(menu, self.basket)

    def view_menu(self):
        return self.menu.formatted_menu()
    
    def add_to_basket(self, item):
        return self.basket.add_to_basket(item)
        # for submenu in self.menu.menu_items.items():
        #     for menu_item in submenu[1]:
        #         if item in list(menu_item):
        #             if menu_item[item]['Stock count'] > 0:
        #                 if item not in self.basket:
        #                     self.basket[item] = 1
        #                     menu_item[item]['Stock count'] -= 1
        #                 else:
        #                     self.basket[item] += 1
        #                     menu_item[item]['Stock count'] -= 1
        #                 return f'{item} has been added to your basket'
        #             else:
        #                 raise Exception('Item out of stock.')
    
    def remove_from_basket(self, item):
        return self.basket.remove_from_basket(item)
        # if self.basket == {}:
        #     raise Exception('No items found in basket')
        # elif item in list(self.basket):
        #     if self.basket[item] > 1:
        #         self.basket[item] -= 1
        #     else:
        #         del self.basket[item]
        #     for submenu in self.menu.menu_items.items():
        #         for menu_item in submenu[1]:
        #             if list(menu_item)[0] == item:
        #                 menu_item[item]['Stock count'] += 1
        #             else:
        #                 pass
        #     return f'{item} has been removed from your basket'
        # else:
        #     return 'Item not found in basket'

    def view_basket(self):
        return self.basket.view_basket()
        # if self.basket == {}:
        #     return 'You have no items in your basket'
        # output = f'The following items are in your basket: '
        # items_string = ', '.join(f'{str(value)} x {key}'  for key, value in self.basket.items())
        # output += items_string
        # return output
    
    def empty_basket(self):
        return self.basket.empty_basket()
    
    def view_itemised_receipt(self):
        return self.receipt.get_receipt()
    
    def place_order(self):
        return 'Please use either customer_login or new_customer.'

# menu = Menu()
# order = Order(menu)
# order.add_to_basket('Cheeseburger')
# order.add_to_basket('Cheeseburger')
# order.remove_from_basket('Cheeseburger')
# order.add_to_basket('Cheeseburger')
