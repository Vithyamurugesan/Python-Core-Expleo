s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

first = s1[0] + s2[0]

middle = s1[len(s1)//2] + s2[len(s2)//2]

last = s1[-1] + s2[-1]

result = first + middle + last

print(result)