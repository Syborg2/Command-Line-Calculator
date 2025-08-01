
def add(x, y):
    """Addition operation"""
    return x + y

def subtract(x, y):
    """Subtraction operation"""
    return x - y

def multiply(x, y):
    """Multiplication operation"""
    return x * y

def divide(x, y):
    """Division operation with zero division handling"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("         COMMAND-LINE CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("-"*40)

def get_numbers():
    """Get two numbers from user input with error handling"""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def get_choice():
    """Get user's menu choice with validation"""
    while True:
        try:
            choice = input("Enter choice (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return '5'

def perform_calculation(choice, num1, num2):
    """Perform the selected calculation"""
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }

    if choice in operations:
        operation_func, symbol = operations[choice]
        result = operation_func(num1, num2)

        if isinstance(result, str):  # Error message
            print(f"\n{result}")
        else:
            print(f"\n{num1} {symbol} {num2} = {result}")

        return True
    return False

def main():
    """Main calculator loop"""
    print("Welcome to the Command-Line Calculator!")

    while True:
        display_menu()
        choice = get_choice()

        if choice == '5':
            print("\nThank you for using the calculator!")
            print("Goodbye! 👋")
            break

        # Get numbers and perform calculation
        print(f"\nYou selected option {choice}")
        num1, num2 = get_numbers()
        perform_calculation(choice, num1, num2)

        # Ask if user wants to continue
        print("\nPress Enter to continue or Ctrl+C to exit...")
        try:
            input()
        except KeyboardInterrupt:
            print("\n\nThank you for using the calculator!")
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()