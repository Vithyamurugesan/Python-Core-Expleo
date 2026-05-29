class Myclass:
    pass

print(Myclass)

obj = Myclass()
obj1 = Myclass()

print(obj)
print(obj1)

def display():
    print("Hi")

def display1(self):                            #No argument
    print("welcome")

def display2(self, name):                      #One argument 
    print("Hello", name)

display()

display1(obj)
display2(obj, "Vithya")