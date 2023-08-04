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