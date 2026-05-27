try:
    fh=open("test.txt",'w')
    #fh=open("invalidpath/test.txt","w")
    try:
        fh.write("this is testing page")
    finally:
       print("Going to close the file")
       fh.close()
except IOError:
    print("Error:cant't find file to read data")
else:
    print("I will exceute when no exception occurs")
finally:
    print("I am executing")