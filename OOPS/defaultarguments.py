class Circle:

    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color

    def getRadius(self):
        return self._radius

    def getColor(self):
        return self._color

    def setRadius(self, radius):
        self._radius = radius

    def setColor(self, color):
        self._color = color

    def getArea(self):
        return 3.14 * self._radius * self._radius

    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"


# Object creation
c1 = Circle()

# Using getter methods
print("Radius :", c1.getRadius())
print("Color  :", c1.getColor())

# Using area method
print("Area   :", c1.getArea())

# Using string method
print(c1)

# Using setter methods
c1.setRadius(5)
c1.setColor("Blue")

print("\nAfter changing values")

# Again using getter methods
print("Radius :", c1.getRadius())
print("Color  :", c1.getColor())

# Again checking area
print("Area   :", c1.getArea())

# Printing object
print(c1)