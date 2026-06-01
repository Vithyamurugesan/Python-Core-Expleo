num = int(input("Enter a number: "))

i = 2

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i = i + 1