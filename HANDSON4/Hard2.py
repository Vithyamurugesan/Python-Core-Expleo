s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""

for i in range(len(s1)):
    result = result + s1[i] + s2[-(i+1)]

print(result)