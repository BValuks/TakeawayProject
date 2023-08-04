import pytest
from lib.menu import Menu
from lib.order import Order
from lib.receipt import Receipt
from lib.basket import Basket

"""
Given an instance of Order
We can view the menu
"""
def test_view_menu_on_order():
    menu = Menu()
    order1 = Order(menu)
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

"""
Given an instance of Order
We can add an item and view it in the basket
"""
def test_add_items_to_basket_and_view_them():
    menu = Menu()
    order1 = Order(menu)
    assert order1.add_to_basket('Cheeseburger') == 'Cheeseburger has been added to your basket'
    assert order1.view_basket() == 'The following items are in your basket: 1 x Cheeseburger'
    order1.add_to_basket('Cheeseburger')
    assert order1.view_basket() == 'The following items are in your basket: 2 x Cheeseburger'
    assert order1.add_to_basket('Onion Rings') == 'Onion Rings has been added to your basket'
    assert order1.view_basket() == 'The following items are in your basket: 2 x Cheeseburger, 1 x Onion Rings'

"""
Given an instance of Order
We can add an item to the basket and see that the available stock has decreased when we view menu
"""
def test_add_menu_item_reduces_stock_count_in_menu():
    menu = Menu()
    order1 = Order(menu)
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '
    order1.add_to_basket('Cheeseburger')
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 4 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

"""
Given an instance of Order
We try and add an item with a stock count of zero and it raises an exception
"""
def test_add_item_with_zero_stock_raises_error():
    menu = Menu()
    order1 = Order(menu)
    order1.view_menu()
    with pytest.raises(Exception) as err:
        order1.add_to_basket('Pulled Pork Burger')
    error_message = str(err.value)
    assert error_message == 'Item out of stock.'

"""
Given an instance of Order
We can remove an item from the basket and the stock count increases to reflect this
"""
def test_remove_item_from_basket_increases_stock_on_menu_items_dict():
    menu = Menu()
    order = Order(menu)
    assert order.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '
    order.add_to_basket('Cheeseburger')
    assert order.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 4 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '
    assert order.view_basket() == 'The following items are in your basket: 1 x Cheeseburger'
    assert order.remove_from_basket('Cheeseburger') == 'Cheeseburger has been removed from your basket'
    assert order.view_basket() == 'You have no items in your basket'
    assert order.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

"""
Given an instance of Order
If we try to remove an item that isn't in the basket, it throws and error
"""
def test_attempt_to_remove_item_not_in_basket_throws_error():
    menu = Menu()
    order = Order(menu)
    order.add_to_basket('Onion Rings')
    assert order.remove_from_basket('Cheeseburger') == 'Item not found in basket'

"""
Given an instance of Order
If we try to remove an item if the basket is empty, it throws an error
"""
def test_attempt_to_remove_item_from_empty_basket():
    menu = Menu()
    order = Order(menu)
    with pytest.raises(Exception) as err:
        order.remove_from_basket('Cheeseburger')
    error_message = str(err.value)
    assert error_message == 'No items found in basket'

"""
Given an instance of Order
Using #empty_basket removes all items in the basket
"""
def test_empty_basket_method_resets_the_basket():
    menu = Menu()
    order = Order(menu)
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Onion Rings')
    assert order.view_basket() == 'The following items are in your basket: 3 x Cheeseburger, 1 x Onion Rings'
    assert order.empty_basket() == 'Basket has been emptied'
    assert order.view_basket() == 'You have no items in your basket'

# """
# Given an instance of Order
# We can view an itemised receipt
# """
# def test_view_itemised_receipt():
#     menu = Menu()
#     order1 = Order(menu)
#     order1.add_to_basket('Cheeseburger')
#     order1.add_to_basket('Onion Rings')
#     order1.add_to_basket('Cheeseburger')
#     assert order1.view_itemised_receipt() == 'Your order: 2 x Cheesburger £20, 1 x Onion Rings £6 | Total: £26'