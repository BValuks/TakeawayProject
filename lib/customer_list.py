from lib.customer import Customer
# from customer import Customer

class CustomerList:
    def __init__(self):
        self.customer_list = []

    def add_customer(self, username, name, phone_number):
        for customer in self.customer_list:
            if customer.username == username:
                raise Exception('Username already in use. Please choose another.')
        customer = Customer(username, name, phone_number)
        self.customer_list.append(customer)
        return f'{name} ({username}) has been added as a customer'
    
    def view_top_customers(self, number):
        output_string = 'Top customers|\n'
        stats = []
        for each in self.customer_list:
            stats.append([each.username, each.name, each.visit_number])
        sorted_stats = sorted(stats, key=lambda customer: customer[2], reverse=True)
        for i in range(number):
            username = sorted_stats[i][0]
            name = sorted_stats[i][1]
            visit_number = sorted_stats[i][2]
            output_string += f'\n * {name} ({username}) - No. of visits: {visit_number}\n'
        return output_string
    
    def view_customers(self):
        customers = [f'{customer.name} ({customer.username})' for customer in self.customer_list]
        return customers
    
    def view_customer_by_username(self, username):
        for customer in self.customer_list:
            if customer.username == username:
                return f'Username: {customer.username}, Name: {customer.name}, Phone number: {customer.phone_number}, Number of visits: {customer.visit_number}'
    
    def remove_customer(self, username):
        for index, customer in enumerate(self.customer_list):
            if customer.username == username:
                name = customer.name
                del self.customer_list[index]
                return f'{name} ({username}) has been removed from the customer list'