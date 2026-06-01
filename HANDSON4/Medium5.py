string1 = input("Enter three words: ")

w1, w2, w3 = string1.split()

print("Default Order:")
print("{} {} {}".format(w1, w2, w3))

print("Positional Order:")
print("{1} {0} {2}".format(w1, w2, w3))

print("Keyword Order:")
print("{c} {b} {a}".format(a=w1, b=w2, c=w3))