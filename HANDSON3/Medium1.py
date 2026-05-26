def odd_sum(lower, upper):
    total = 0
    for i in range(lower, upper + 1):
        if i % 2 != 0:
            total += i
    return total

def even_sum(lower, upper):
    total = 0
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            total += i
    return total
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

odd_total = odd_sum(lower, upper)
even_total = even_sum(lower, upper)
difference = abs(odd_total - even_total)
print("The sum of odd numbers from", lower, "to", upper, "is:", odd_total)
print("The sum of even numbers from", lower, "to", upper, "is:", even_total)
print("The absolute difference between the two sums is:", difference)