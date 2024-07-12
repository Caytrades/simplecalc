# # Add
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Added Answer:", x + y)

# # Subtract
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Subtracted Answer:", x - y)


# # Multiply
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Multiplied Answer:", x * y)

# # Divide
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Divide Answer:", int(x / y))


#Give the user the option to add substract, divide and multiply

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


#Options for user
print("1.Add")
print("2.Sub")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter a choice:(1/2/3/4)")

    if choice in ['1','2','3','4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1,num2)}")
        # print(add(num1, num2))
    elif choice == '2':
        print(f"{num1} - {num2} = {substract(num1,num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1,num2)}")
    else:
        print("Invalid")
    break




