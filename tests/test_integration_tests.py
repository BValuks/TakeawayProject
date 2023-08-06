import pytest
from lib.menu import Menu
from lib.order import Order
from lib.receipt import Receipt
from lib.basket import Basket
from lib.customer_list import CustomerList

"""
Given an instance of Order
We can view the menu
"""
def test_view_menu_on_order():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

"""
Given an instance of Order
We can add an item and view it in the basket
"""
def test_add_items_to_basket_and_view_them():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
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
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 5 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '
    order1.add_to_basket('Cheeseburger')
    assert order1.view_menu() == 'Menu items:\n\n * Burgers| \n - Cheeseburger, Price: 10.0, Available: 4 \n - Pulled Pork Burger, Price: 12.0, Available: 0 \n - Chicken Burger, Price: 10.5, Available: 5 \n - Halloumi Burger, Price: 9.0, Available: 4 \n - Jackfruit Burger, Price: 9.5, Available: 3 \n\n * Sides| \n - Onion Rings, Price: 6.0, Available: 10 \n - Skin-on-fries, Price: 4.0, Available: 25 \n - Chilli Cheese Bites, Price: 6.5, Available: 8 \n - Side Salad, Price: 4.0, Available: 20 \n\n * Drinks| \n - Coke, Price: 2.4, Available: 24 \n - Water, Price: 2.0, Available: 18 \n - Beer, Price: 5.25, Available: 24 '

"""
Given an instance of Order
We try and add an item with a stock count of zero and it raises an exception
"""
def test_add_item_with_zero_stock_raises_error():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
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
    customer_list = CustomerList()
    order = Order(menu, customer_list)
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
    customer_list = CustomerList()
    order = Order(menu, customer_list)
    order.add_to_basket('Onion Rings')
    assert order.remove_from_basket('Cheeseburger') == 'Item not found in basket'

"""
Given an instance of Order
If we try to remove an item if the basket is empty, it throws an error
"""
def test_attempt_to_remove_item_from_empty_basket():
    menu = Menu()
    customer_list = CustomerList()
    order = Order(menu, customer_list)
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
    customer_list = CustomerList()
    order = Order(menu, customer_list)
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Onion Rings')
    assert order.view_basket() == 'The following items are in your basket: 3 x Cheeseburger, 1 x Onion Rings'
    assert order.empty_basket() == 'Basket has been emptied'
    assert order.view_basket() == 'You have no items in your basket'

"""
Given an instance of Order
We can view an itemised receipt
"""
def test_view_itemised_receipt():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
    order1.add_to_basket('Cheeseburger')
    order1.add_to_basket('Onion Rings')
    order1.add_to_basket('Cheeseburger')
    assert order1.view_itemised_receipt() == 'Itemised receipt:\n Cheeseburger x 2 = 20.0\n Onion Rings x 1 = 6.0\n\n Grand total = 26.0'

"""
Given an instance of Order
We place an order and we're told to login or set up a new customer
"""
def test_when_placing_order_we_are_told_to_login_or_setup_new_customer():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
    order1.add_to_basket('Cheeseburger')
    assert order1.place_order() == 'Please use either customer_login or new_customer.'

"""
Given an instance of Order
We place an order with a customer supplied with #new_customer
"""
def test_order_placed_with_new_customer():
    menu = Menu()
    customer_list = CustomerList()
    order1 = Order(menu, customer_list)
    order1.add_to_basket('Cheeseburger')
    order1.new_customer('BenV', 'Benedict', '07965430788')
    assert order1.place_order() == 'Thank you for your order Benedict. You should receive text confirmation soon.'

"""
Given an instance of Order
We place an order with a customer supplied with #customer_login
"""
def test_order_placed_with_customer_login():
    menu = Menu()
    customer_list = CustomerList()
    assert customer_list.add_customer('BenV', 'Benedict', '07965430788') == 'Benedict (BenV) has been added as a customer'
    order1 = Order(menu, customer_list)
    order1.add_to_basket('Cheeseburger')
    assert order1.customer_login('BenV') == 'Welcome back Benedict'
    assert order1.place_order() == 'Thank you for your order Benedict. You should receive text confirmation soon.'

"""
Given an instance of CustomerList
We can call #view_top_customers and see the top customers by number of visits and see popular dishes
"""
def test_view_top_customers_by_visit_numbers_and_view_popular_dishes():
    menu = Menu()
    customer_list = CustomerList()
    customer_list.add_customer('BVal', 'Benedict', '07965430788')
    customer_list.add_customer('LizA', 'Lizzie', '02084536661')
    customer_list.add_customer('NoahV', 'Noah', '07264009867')
    customer_list.add_customer('Simyarn', 'Simeon', '07839104213')

    order_benedict1 = Order(menu, customer_list)
    order_lizzie1 = Order(menu, customer_list)
    order_noah1 = Order(menu, customer_list)
    order_simeon1 = Order(menu, customer_list)

    order_benedict1.add_to_basket('Cheeseburger')
    order_benedict1.customer_login('BVal')
    order_benedict1.place_order()

    order_benedict2 = Order(menu, customer_list)
    order_benedict2.add_to_basket('Cheeseburger')
    order_benedict2.customer_login('BVal')
    order_benedict2.place_order()

    order_lizzie1.add_to_basket('Onion Rings')
    order_lizzie1.customer_login('LizA')
    order_lizzie1.place_order()

    order_noah1.add_to_basket('Coke')
    order_noah1.customer_login('NoahV')
    order_noah1.place_order()

    order_noah2 = Order(menu, customer_list)
    order_noah2.add_to_basket('Coke')
    order_noah2.customer_login('NoahV')
    order_noah2.place_order()

    order_noah3 = Order(menu, customer_list)
    order_noah3.add_to_basket('Coke')
    order_noah3.customer_login('NoahV')
    order_noah3.place_order()

    order_noah4 = Order(menu, customer_list)
    order_noah4.add_to_basket('Coke')
    order_noah4.customer_login('NoahV')
    order_noah4.place_order()

    order_simeon1.add_to_basket('Chicken Burger')
    order_simeon1.customer_login('Simyarn')
    order_simeon1.place_order()

    order_simeon2 = Order(menu, customer_list)
    order_simeon2.add_to_basket('Chicken Burger')
    order_simeon2.customer_login('Simyarn')
    order_simeon2.place_order()

    order_simeon3 = Order(menu, customer_list)
    order_simeon3.add_to_basket('Chicken Burger')
    order_simeon3.customer_login('Simyarn')
    order_simeon3.place_order()

    assert customer_list.view_top_customers(2) == 'Top customers|\n\n * Noah (NoahV) - No. of visits: 4\n\n * Simeon (Simyarn) - No. of visits: 3\n' 
    assert customer_list.view_top_customers(3) == 'Top customers|\n\n * Noah (NoahV) - No. of visits: 4\n\n * Simeon (Simyarn) - No. of visits: 3\n\n * Benedict (BVal) - No. of visits: 2\n'
    assert customer_list.view_top_customers(4) == 'Top customers|\n\n * Noah (NoahV) - No. of visits: 4\n\n * Simeon (Simyarn) - No. of visits: 3\n\n * Benedict (BVal) - No. of visits: 2\n\n * Lizzie (LizA) - No. of visits: 1\n'

    order1 = Order(menu, customer_list)
    assert order1.view_popular_items() == 'Top items: \n1. Coke\n2. Chicken Burger\n3. Cheeseburger\n'


"""
Given an instance of CustomerList
We can add some customers and view them as a list and by searching by customer and then remove a customer
"""
def test_add_customers_to_customer_list_view_them_and_removed_them():
    customer_list = CustomerList()
    assert customer_list.add_customer('BVal', 'Benedict', '07965430788') == 'Benedict (BVal) has been added as a customer'
    assert customer_list.add_customer('LizA', 'Lizzie', '02084536661') == 'Lizzie (LizA) has been added as a customer'
    assert customer_list.view_customers() == ['Benedict (BVal)', 'Lizzie (LizA)']
    assert customer_list.view_customer_by_username('LizA') == 'Username: LizA, Name: Lizzie, Phone number: 02084536661, Number of visits: 0'
    assert customer_list.remove_customer('BVal') == 'Benedict (BVal) has been removed from the customer list'
    assert customer_list.view_customers() == ['Lizzie (LizA)']

"""
Given an instance of CustomerList
Attempting to add a new customer with a username that is not unique throws an error
"""
def test_attempt_to_add_new_customer_with_a_name_that_is_not_unique():
    customer_list = CustomerList()
    customer_list.add_customer('BenV', 'Benedict', '07965430788')
    customer_list.add_customer('LizA', 'Lizzie', '02084536661')
    with pytest.raises(Exception) as err:
        customer_list.add_customer('BenV', 'Benjamin', '01805787254')
    error_message = str(err.value)
    assert error_message == 'Username already in use. Please choose another.'

"""
Given an instance of Menu
We can use #view_items_sold to view items and amount of items sold and use #reset_items_sold to reset the items sold list
"""
def test_view_items_sold_and_reset_the_list():
    menu = Menu()
    customer_list = CustomerList()
    order = Order(menu, customer_list)
    order.add_to_basket('Cheeseburger')
    order.add_to_basket('Onion Rings')
    order.add_to_basket('Cheeseburger')
    assert order.view_basket() == 'The following items are in your basket: 2 x Cheeseburger, 1 x Onion Rings'
    order.new_customer('BVal', 'Benedict', '07123456789')
    order.place_order()
    assert menu.view_items_sold() == {'Cheeseburger': 2, 'Onion Rings': 1}
    assert menu.reset_items_sold() == 'Items sold reset'
    assert menu.view_items_sold() == {}