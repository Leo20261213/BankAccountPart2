#main.py

from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():
    print("=== BackAccount Inheritance Program ===")

    # Create two savings accounts.

    sav1 = SavingsAccount("Alice", 2000, 100, 0.05)
    sav2 = SavingsAccount("Bob", 1500, 100, 0.33)

    # Create two checking accounts.

    chk1 = CheckingAccount("Charlie", 1200, 50, 500)
    chk2 = CheckingAccount("Diana", 800, 50, 300)

    # Scenario 1: Charlie withdraws money

    print("\n--- Scenario 1: Charlie withdraws $200 ---")
    chk1.withdraw(200)

    # Scenario 2: Alice earns interest

    print("\n--- Scenario 2: Alice earns interest ---")

    # Scenario 3: Charlie transfers money to Diana.

    print("\n--- Scenario 3: Charlie transfers $300 to Diana ---")

    # Print the account information

    print("\n--- Final Account Information --")
    sav1.print_account_info()
    sav2.print_account_info()
    chk1.print_account_info()
    chk2.print_account_info()

if __name__ == "__main__":
    main()