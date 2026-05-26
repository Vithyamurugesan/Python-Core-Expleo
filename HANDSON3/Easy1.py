def sum_odd_even(n):
    even_sum = 0
    odd_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print("Sum of Even Numbers:", even_sum)
    print("Sum of Odd Numbers:", odd_sum)
num = int(input("Enter a number: "))
sum_odd_even(num)