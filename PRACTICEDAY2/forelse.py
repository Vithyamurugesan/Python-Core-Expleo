L=int(input("Enter Lower limit:"))
U=int(input("Enter Upper limit"))
print("the prime numbers between",L,"and",U,"are")
for num in range(L,U+1):
    if num>1:#prime number are greater than 1
        for i in range(2,num):
            if(num%i)==0:
                break
        else:#for-else
            print(num)
