try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b
except NameError:
    print("this is value error")
except Exception:
    print("cant divide with zero")
    print(Exception)
else:
   print("Excuted successfully with no exception")
finally:
    print("excuted")