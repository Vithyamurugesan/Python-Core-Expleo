count = 0
total = 0

min_price = 101
max_price = 0

while True:
    price = int(input())

    if price == -1:
        break

    if price < min_price:
        min_price = price

    if price > max_price:
        max_price = price

    if 5 <= price <= 30:
        total = total + price
        count = count + 1

average = total // count

print(max_price, min_price, average)