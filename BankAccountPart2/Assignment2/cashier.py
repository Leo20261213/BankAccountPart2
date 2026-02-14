#cashier.py

class Cashier:
    def process_coins(self):
        """Return total amount of money inserted."""
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickels + pennies

    def transaction_result(self, money_received, cost):
        """Return True if payment is accepted, otherwise False."""
        if money_received < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif money_received > cost:
            change = round(money_received - cost, 2)
            print(f"Here is ${change} in change.")
        return True
