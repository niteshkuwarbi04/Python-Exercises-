'''
4. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item,
   update_item, and check_item_details. Use a dictionary to store the item details, where the key is the item_id and the 
   value is a dictionary containing the item_name, stock_count, and price.'''

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price}
            print(f"Item {item_name} added to inventory with ID {item_id}.")
        else:
            print(f"Item ID {item_id} already exists in the inventory. Use update_item to modify details.")

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            if item_name is not None:
                self.items[item_id]['item_name'] = item_name
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Item {item_id} details updated.")
        else:
            print(f"Item ID {item_id} not found in the inventory. Use add_item to add a new item.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            item_details = self.items[item_id]
            print(f"Item ID: {item_id}")
            print(f"Item Name: {item_details['item_name']}")
            print(f"Stock Count: {item_details['stock_count']}")
            print(f"Price: ${item_details['price']}")
        else:
            print(f"Item ID {item_id} not found in the inventory.")

# Create an instance of the Inventory class
inventory = Inventory()

# Perform operations on the inventory
inventory.add_item("001", "Laptop", 10, 800)
inventory.add_item("002", "Printer", 5, 150)
inventory.update_item("001", stock_count=8)
inventory.check_item_details("001")
inventory.check_item_details("003")  # Non-existent item
