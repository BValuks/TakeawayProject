from lib.menu import Menu
from unittest.mock import Mock

def test_formatted_menu_returns_formatted_menu():
    menu = Menu()
    assert menu.formatted_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

def popular_items_returns_top_3_best_selling_items():
    self.items_sold = Mock()
    self.items_sold.return_value = {'Cheeseburger': 2, 'Onion Rings': 1, 'Coke': 3}
    menu = Menu()
    assert menu.popular_items() == 'Top items: \n1. Coke\n2. Cheeseburger\n3. Onion Rings\n'