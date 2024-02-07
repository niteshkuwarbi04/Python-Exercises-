'''
2.  Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
    Perform the following tasks now:
    Now add items to the menu.
    Make table reservations.
    Take customer orders.
    Print the menu.
    Print table reservations.
    Print customer orders.'''

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = {}

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} booked successfully.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, items):
        if table_number not in self.customer_orders:
            self.customer_orders[table_number] = items
            print(f"Order for Table {table_number} received successfully.")
        else:
            print(f"Table {table_number} already has an order.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_booked_tables(self):
        print("Booked Tables:", self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, items in self.customer_orders.items():
            print(f"Table {table}: {items}")

# Create an instance of the Restaurant class
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Burger", 10)
restaurant.add_item_to_menu("Pizza", 15)
restaurant.add_item_to_menu("Pasta", 12)

# Make table reservations
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(1)  # Trying to book the same table again

# Take customer orders
restaurant.customer_order(1, ["Burger", "Pizza"])
restaurant.customer_order(2, ["Pasta", "Burger"])

# Print menu, table reservations, and customer orders
restaurant.print_menu()
restaurant.print_booked_tables()
restaurant.print_customer_orders()
