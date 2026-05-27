fobj=open("myfile.txt",'w')
str=input("Enter the string to write it in the file: ")
fobj.write(str)

fobj=open("myfile.txt",'r')
for str in fobj:
    print(str)
print("readed successfully")
fobj.close()


