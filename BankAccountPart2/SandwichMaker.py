class SandwichMachine:
    def __init__(self, machine_resources):
        self.resources = machine_resources

        self.recipes = {
            "small": {
                "ingredients": {"bread": 2, "ham": 4, "cheese": 4},
                "cost": 1.75
            },
            "medium": {
                "ingredients": {"bread": 4, "ham": 6, "cheese": 8},
                "cost": 3.25
            },
            "large": {
                "ingredients": {"bread": 6, "ham": 8, "cheese": 12},
                "cost": 5.5
            }
        }

    def check_resources(self, ingredients):
        """Return True if resources are sufficient, otherwise False."""
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Return total amount of money inserted."""

        def get_int(prompt):
            while True:
                value = input(prompt)
                try:
                    num = int(value)
                    if num < 0:
                        print("Please enter a non-negative whole number.")
                    else:
                        return num
                except ValueError:
                    print("Please enter a whole number (0, 1, 2, ...).")

        print("Please insert coins.")
        dollars = get_int("how many large dollars?: ") * 1.00
        half_dollars = get_int("how many half dollars?: ") * 0.50
        quarters = get_int("how many quarters?: ") * 0.25
        nickels = get_int("how many nickels?: ") * 0.05

        return dollars + half_dollars + quarters + nickels


    def transaction_result(self, coins, cost):
        """Return True if payment accepted, otherwise False."""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct ingredients from resources and make the sandwich."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.resources['bread']} slice(s)")
        print(f"Ham: {self.resources['ham']} slice(s)")
        print(f"Cheese: {self.resources['cheese']} pound(s)")


def main():
    machine_resources = {
        "bread": 12,
        "ham": 18,
        "cheese": 24
    }

    machine = SandwichMachine(machine_resources)

    running = True

    try:
        while running:
            choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

            if choice == "off":
                running = False

            elif choice == "report":
                machine.report()

            elif choice in machine.recipes:
                recipe = machine.recipes[choice]
                ingredients = recipe["ingredients"]
                cost = recipe["cost"]

                if machine.check_resources(ingredients):
                    coins = machine.process_coins()
                    if machine.transaction_result(coins, cost):
                        machine.make_sandwich(choice, ingredients)

            else:
                print("Invalid selection. Try again.")

    except KeyboardInterrupt:
        print("\nMachine shutting down safely...")

if __name__ == "__main__":
    main()
