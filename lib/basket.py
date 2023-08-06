class Basket():
    def __init__(self, menu):
        self.menu = menu
        self.basket = {} # example: {'Cheeseburger': 1}
        
    def view_basket(self):
        if self.basket == {}:
            return 'You have no items in your basket'
        output = f'The following items are in your basket: '
        items_string = ', '.join(f'{str(value)} x {key}'  for key, value in self.basket.items())
        output += items_string
        return output

    def add_to_basket(self, item):
        for submenu in self.menu.menu_items.items():
            for menu_item in submenu[1]:
                if item in list(menu_item):
                    if menu_item[item]['Stock count'] > 0:
                        if item not in self.basket:
                            self.basket[item] = 1
                            menu_item[item]['Stock count'] -= 1
                        else:
                            self.basket[item] += 1
                            menu_item[item]['Stock count'] -= 1
                        return f'{item} has been added to your basket'
                    else:
                        raise Exception('Item out of stock.')

    def remove_from_basket(self, item):
        if self.basket == {}:
            raise Exception('No items found in basket')
        elif item in list(self.basket):
            if self.basket[item] > 1:
                self.basket[item] -= 1
            else:
                del self.basket[item]
            for submenu in self.menu.menu_items.items():
                for menu_item in submenu[1]:
                    if list(menu_item)[0] == item:
                        menu_item[item]['Stock count'] += 1
                    else:
                        pass
            return f'{item} has been removed from your basket'
        else:
            return 'Item not found in basket'
    
    def empty_basket(self):
        self.basket = {}
        return 'Basket has been emptied'
    
    def items_ordered(self):
        for item in self.basket:
            if item not in self.menu.items_sold:
                self.menu.items_sold[item] = self.basket[item]
            elif item in self.menu.items_sold:
                self.menu.items_sold[item] += 1