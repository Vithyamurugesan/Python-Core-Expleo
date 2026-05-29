class MyClass:
    x=5   #State
    def display(self): #Behaviour
        print("I am inside the function")
obj=MyClass()
print('State:',obj.x)
print('Behaviour:')
obj.display()