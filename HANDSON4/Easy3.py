str1 = input("Enter a string: ")
result = ""

for ch in str1:
    if ch.isalnum() or ch.isspace():
        result += ch
    else:
        result += "#"

print(result)