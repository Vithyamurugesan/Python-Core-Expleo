total_price = 0
count = 1
while True:
    price = int(input("Enter the price of item: "))
    quantity = int(input("Enter the quantity: "))
    total_price += price * quantity
    choice = input("Do you want to enter another item? (yes/no): ")
    if choice.lower() == "no":
        break
print("Total Price:", total_price)