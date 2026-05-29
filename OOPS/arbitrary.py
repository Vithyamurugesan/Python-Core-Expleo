# Handling Variable Arguments

class Circle:

    def __init__(self, *args):

        if len(args) == 0:
            self.__radius = 1.0
            self.__color = "red"

        elif len(args) == 1:
            self.__radius = args[0]
            self.__color = "red"

        elif len(args) == 2:
            self.__radius = args[0]
            self.__color = args[1]

        else:
            raise ValueError("Too many arguments")

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def getArea(self):
        return 3.14 * self.__radius * self.__radius

    def __str__(self):
        return f"Circle[radius={self.__radius}, color={self.__color}]"


circle1 = Circle()
print(circle1)

circle2 = Circle(2.5)
print(circle2)

circle3 = Circle(3.5, "blue")
print(circle3)