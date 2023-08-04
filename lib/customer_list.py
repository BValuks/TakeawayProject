from lib.customer import Customer

class CustomerList:
    def __init__(self):
        self.customer_list = []

    def add_customer(self, username, name, phone_number):
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
