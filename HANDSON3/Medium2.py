def print_primes(x, y):
    for num in range(x, y + 1):
        if num > 1:
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                print(num, end=" ")

x = int(input("Enter starting number: "))
y = int(input("Enter ending number: "))
if x > y:
    print("Provide valid input")

else:
    print_primes(x, y)