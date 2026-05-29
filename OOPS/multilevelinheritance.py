class Student:
    def getStudentInfo(self):
        self.__rollno=input("enter roll number")
        self.__name=input("enter name")
    def printStudentInfo(self):
        print("Roll number",self.__rollno,"Name",self.__name)
class Marks(Student):
    def getmarks(self):
        self.getStudentInfo()
        self.__mark1=float(input("enter the marks for sub 1"))
        self.__mark2=float(input("enter the marks for sub 2"))
        self.__mark3=float(input("enter the marks for sub 3"))
    def printmarks(self):
        self.printStudentInfo()
        print("Mark 1",self.__mark1)
        print("Mark 2",self.__mark2)
        print("Mark 3",self.__mark3)
    def calcTotalMarks(self):
        return self.__mark1+self.__mark2+self.__mark3
class Result(Marks):
    def getResult(self):
        self.getmarks()
        self.__total=self.calcTotalMarks()
    def putResult(self):
        self.printmarks()
        print("total marks out of 300:",self.__total)
obj=Result()
obj.getResult()
obj.putResult()
