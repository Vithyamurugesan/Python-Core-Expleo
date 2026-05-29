class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age    #private member
    def get_age(self):
        return self.__age
    def set_age(self,age): #setter method
        self.__age=age
stud=Student("mary",14)
print("Name:",stud.name,stud.get_age())
#retreiving age using getter
stud.set_age(16)
print("Name:",stud.name,stud.get_age())
#retreiving age using getter
