try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b;
except(ZeroDivisionError):
    print("cant divide with zero")
else:
   print("Excuted successfully with no exception")
