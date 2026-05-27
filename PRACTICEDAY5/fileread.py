my = open("myfile.txt", "r")
var=my.read(10)
#var=my.read(-1)    it will read all 
#var=my.read()      it will read all
print(var)

my.close()
