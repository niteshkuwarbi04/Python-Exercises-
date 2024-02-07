'''
3. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and 
   methods like deposit, withdraw, and check_balance.'''

import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = datetime.date.today()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

    def check_balance(self):
        print(f"Account Balance for {self.customer_name}: ${self.balance}")

# Create an instance of the BankAccount class
account1 = BankAccount("123456789", "John Doe", 1000)

# Perform operations on the account
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
