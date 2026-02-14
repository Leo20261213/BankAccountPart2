# main.py

import data
import sandwich_maker
import cashier

def main():
    resources = data.resources
    recipes = data.recipes

    maker = sandwich_maker.SandwichMaker(resources)
    cash = cashier.Cashier()

    machine_on = True

    while machine_on:
        choice = input("What size sandwich would you like? (small/medium/large/report/off): ").lower()

        if choice == "off":
            machine_on = False

        elif choice == "report":
            print(f"Bread: {resources['bread']}")
            print(f"Ham: {resources['ham']}")
            print(f"Cheese: {resources['cheese']}")

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if maker.check_resources(ingredients):
                payment = cash.process_coins()
                if cash.transaction_result(payment, cost):
                    maker.make_sandwich(choice, ingredients)

        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
