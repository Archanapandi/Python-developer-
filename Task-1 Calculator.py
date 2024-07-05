def add(x, y):
    """Add two numbers"""
    return x + y

def sub(x, y):
    """Subtract two numbers"""
    return x - y

def mul(x, y):
    """Multiply two numbers"""
    return x * y

def div(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculate(operation, num1, num2):
    """Evaluate a mathematical expression"""
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return sub(num1, num2)
    elif operation == "*":
        return mul(num1, num2)
    elif operation == "/":
        return div(num1, num2)
    else:
        raise ValueError("Invalid operator!")

def main():
    """Command-line interface for the calculator"""
    print("Welcome to the Text Calculator!")
    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculate("+", num1, num2)
                print(f"Result: {result:.2f}")
            elif choice == 2:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculate("-", num1, num2)
                print(f"Result: {result:.2f}")
            elif choice == 3:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculate("*", num1, num2)
                print(f"Result: {result:.2f}")
            elif choice == 4:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculate("/", num1, num2)
                print(f"Result: {result:.2f}")
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()