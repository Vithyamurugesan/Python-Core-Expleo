def fact(num):
    if num==0:
        return 1
    else:
        return(num*fact(num-1))
num=int(input("Enter any number :"))
fact=fact(num)
print("The fact of ",num,"is",fact)
