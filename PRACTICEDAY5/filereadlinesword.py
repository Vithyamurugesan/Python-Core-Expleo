my = open("myfile.txt", "r")
var=my.readlines()
for line in var:
    words=line.split()
    print(words)
my.close()

print()


my = open("myfile.txt", "r")
var=my.readlines()
for line in var:
    words=line.splitlines()
    print(words)
my.close()