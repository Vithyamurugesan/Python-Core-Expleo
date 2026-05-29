class student:
    def __init__(self):
        self.name="vithya"  #public
        self.__age=39       #private
obj=student()
print(obj.name)      #calling using object ref.of student 
print(obj._age)      #calling using private variable
