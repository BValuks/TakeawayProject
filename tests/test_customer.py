from lib.customer import Customer

"""
Given an instance of Customer
We can use #view_username, #view_name, #view_phone_number to view those variables 
"""
def test_initialise_customer_class_with_class_variables():
    customer = Customer('BVal', 'Benedict', '07123456789')
    assert customer.view_username() == 'BVal'
    assert customer.view_name() == 'Benedict'
    assert customer.view_phone_number() == '07123456789'

"""
Given an instance of Customer
We can use #update_username, #update_name, #update_phone_number to update those variables 
"""
def test_update_methods_update_class_variables():
    customer = Customer('BVal', 'Benedict', '07123456789')
    assert customer.update_username('LizA') == 'Your username has been changed to LizA'
    assert customer.update_name('Lizzie') == 'Your name has been changed to Lizzie'
    assert customer.update_phone_number('07987654321') == 'Your phone number has been changed to 07987654321'
    assert customer.view_username() == 'LizA'
    assert customer.view_name() == 'Lizzie'
    assert customer.view_phone_number() == '07987654321'