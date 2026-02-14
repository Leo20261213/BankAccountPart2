# sandwich_maker.py

class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        """Return True if resources are sufficient, otherwise False."""
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, ingredients):
        """Deduct ingredients from resources."""
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {sandwich_size} ham sandwich! Enjoy!")
