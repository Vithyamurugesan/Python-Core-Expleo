listA=[]
n=int(input("Enter the number of elements in the list : "))
for i in range(0,n):
    print("Enter elements No-{}:".format(i+1))
    elm=int(input())
    listA.append(elm) #adding the element
    print("The entered list is: \n",listA)
    