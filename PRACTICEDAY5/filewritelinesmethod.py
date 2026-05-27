my = open("myfile.txt", "w")
lines=["Hello everyone\n","Writting #multiline strings\n","This is the #third line"]
my.writelines(lines)
print("written")
my.close()