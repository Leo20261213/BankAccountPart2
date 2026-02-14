#savings_account.py

'''
This child class extends the parent BankAccount and has additional functionality for
applying interest.
'''
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, balance, minimum_balance, interest_rate):
        super().__init__(customer_name, balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self._balance:.2f}")
