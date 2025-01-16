# a simple calculator

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

operation = input("Enter the operation: ")

if operation == "+":
    print("result ", int(first_number) + int(second_number))
if operation == "-":
    print("result ", int(first_number) - int(second_number))
if operation == "*":
    print("result ", int(first_number) * int(second_number))
if operation == "/":
    print("result ", int(first_number) / int(second_number))
print("Thank you for using our calculator")