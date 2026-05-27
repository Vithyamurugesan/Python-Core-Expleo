try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b;
except(ZeroDivisionError):
    print("cant divide with zero")
print("Sucsessfuly excuted")
