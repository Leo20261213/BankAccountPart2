#checking_account.py

from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, balance, minimum_balance)
        self.transfer_limit = transfer_limit

        def transfer(self, amount, target_account):
            if amount > self.transfer_limit:
                print(f"Transfer denied. Amount exceeds transfer limit of ${self.transfer_limit}")
            elif amount <= 0:
                print("Transfer amount must be positive.")
            elif self._balance - amount < self.minimum_balance:
                print("Transfer denied. Insufficient funds.")
            else:
                self._balance -= amount
                target_account._balance += amount
                print(f"Transferred ${amount} to {target_account.customer_name}.")
                print(f"New Balance: ${self._balance}")