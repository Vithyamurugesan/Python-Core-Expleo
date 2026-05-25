name = input("Enter customer name: ")

items = int(input("Enter number of items: "))

if items < 10:
    total_cost = items * 12

elif items < 100:
    total_cost = items * 10

else:
    total_cost = items * 7

print(name, total_cost)