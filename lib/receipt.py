# from menu import Menu
# from basket import Basket

class Receipt:
    def __init__(self, menu, basket):
        self.menu = menu
        self.basket = basket

    def get_receipt(self):
        formatted_receipt = 'Itemised receipt:'
        grand_total = 0
        for submenu in self.menu.menu_items.items():
            for menu_item in submenu[1]:
                for entry in menu_item.items():
                    if entry[0] in list(self.basket.basket):
                        amount_sold = self.basket.basket[list(menu_item)[0]]
                        item_price = entry[1]["Price"]
                        formatted_receipt += f'\n {entry[0]} x {amount_sold} = {amount_sold * item_price}'
                        grand_total += amount_sold * item_price
                    else:
                        pass
        formatted_receipt += f'\n\n Grand total = {grand_total}'
        return formatted_receipt


# menu = Menu()
# basket = Basket(menu)
# receipt = Receipt(menu, basket)
# receipt.get_receipt()