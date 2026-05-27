import traceback
try:
    num=int(input("enter the positive integer"))
    if(num<=0):
        raise ValueError("this is a negative value")
except ValueError as e:
    traceback.print_exc()
    print(e)
print("i am successfully handled")