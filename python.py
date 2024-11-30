print("Select an operation to perform:")
print("1. ADDITION")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input("Enter choice (1/2/3/4): ")

if operation == '1':  # Comparing as a string, since input() returns a string
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The sum is: " + str(num1 + num2))

elif operation == '2':  # For subtraction
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The difference is: " + str(num1 - num2))

elif operation == '3':  # For multiplication
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The product is: " + str(num1 * num2))

elif operation == '4':  # For division
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        print("The Answer is: " + str(num1 / num2))
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid entry. Please choose a valid operation (1/2/3/4).")
