string=input("Enter string : ")
total_digits=0
total_letters=0
for s in string:
    if s.isnumeric():
        total+=1
    elif s.isalpha():
        total_letters+=1
    else:
        pass
print("Total letters found",total_letters)
print("Total didgits found",total_digits)