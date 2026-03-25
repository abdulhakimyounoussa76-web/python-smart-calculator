def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def calculator():
    print("=== Smart Calculator ===")
    print("Operations: +  -  *  /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operation")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        again = input("Do you want to continue? (y/n): ").lower()
        if again != "y":
            print("Calculator closed.")
            break


calculator()
