str1 = input("Enter a string: ")

lower = ""
upper = ""

for ch in str1:
    if ch.islower():
        lower += ch
    else:
        upper += ch

print(lower + upper)