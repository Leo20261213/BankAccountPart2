# bank_account.py

'''
This is the parent class called BankAccount that is carried from the initial BankAccount exercise.
'''
class BankAccount:
    def __init__(self, customer_name, balance, minimum_balance):
        self.customer_name = customer_name
        self._balance = balance                 # protected member
        self.__account_number = "123456789"     # private member
        self.__routing_number = "987654321"     # private member
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.customer_name} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self._balance - amount >= self.minimum_balance:
            self._balance -= amount
            print(f"{self.customer_name} withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Withdrawal denied. Balance would fall below minimum.")

    def print_account_info(self):
        print(f"Customer: {self.customer_name}")
        print(f"Balance: ${self._balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self.__routing_number}")
