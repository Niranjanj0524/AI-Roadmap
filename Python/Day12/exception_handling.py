import sys

class InvalidChoiceError(Exception): pass
class ZeroAmountError(Exception): pass
class NegativeAmountError(Exception): pass
class InsufficientBalanceError(Exception): pass
class LargeAmountError(Exception): pass

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Error: Input cannot be empty.")
            continue
        if "e" in user_input.lower():
            print("Error: Scientific notation is not allowed.")
            continue
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def validate_transaction(amount, balance=None):
    if amount == 0:
        raise ZeroAmountError("Error: Amount cannot be zero.")
    if amount < 0:
        raise NegativeAmountError("Error: Amount cannot be negative.")
    if amount > 100000000:
        raise LargeAmountError("Error: Amount exceeds maximum single transaction limit of $100,000,000.")
    if balance is not None and amount > balance:
        raise InsufficientBalanceError(f"Error: Insufficient balance. Current Balance: ${balance:.2f}")

def atm_simulation():
    balance = 1000.0
    
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice not in ["1", "2", "3", "4"]:
                raise InvalidChoiceError("Error: Invalid menu choice. Please select 1, 2, 3, or 4.")
                
            if choice == "1":
                print(f"Current Balance: ${balance:.2f}")
                
            elif choice == "2":
                amount = get_numeric_input("Enter deposit amount: ")
                validate_transaction(amount)
                balance += amount
                print(f"Successfully deposited ${amount:.2f}. New Balance: ${balance:.2f}")
                
            elif choice == "3":
                amount = get_numeric_input("Enter withdrawal amount: ")
                validate_transaction(amount, balance)
                balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. New Balance: ${balance:.2f}")
                
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                sys.exit()
                
        except (InvalidChoiceError, ZeroAmountError, NegativeAmountError, InsufficientBalanceError, LargeAmountError) as e:
            print(e)

atm_simulation()
