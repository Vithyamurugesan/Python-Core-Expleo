code = int(input("Enter code: "))
if code == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(num1 + num2)
elif code == 2:

    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    print(num1 * num2)
elif code == 3:

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    print(str1 + str2)
else:
    print("Invalid Code")