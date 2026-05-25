def circle(radius):
    print("Area of circle: ",3.14*radius*radius)
def rectangle(length,breadth):
    print("Area of Rectangle: ",length*breadth)
def square(side):
    print("Area: ",side*side)
while True:
    print("Menu driven Program")
    print("1.Area of circle")
    print("2.Area of Rectangle")
    print("3.Area of Square")
    print("4.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        rad=int(input())
        circle(rad)
    elif choice==2:
        len=int(input())
        bre=int(input())
        rectangle(len,bre)
    elif choice==3:
        side=int(input())
        square(side)
    elif choice==4:
        break
    else:
        print("Exit..")
