# Using class method for named constructors
class Circle:
    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color
    # Named constructor with only radius
    @classmethod
    def withRadius(cls, radius):
        return cls(radius)
    # Named constructor with radius and color
    @classmethod
    def withRadiusAndColor(cls, radius, color):
        return cls(radius, color)
    # Getter method for radius
    def getRadius(self):
        return self._radius
    # Getter method for color
    def getColor(self):
        return self._color
    # String representation
    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"

# Object using default constructor
c1 = Circle()

# Object using named constructor with radius
c2 = Circle.withRadius(5)

# Object using named constructor with radius and color
c3 = Circle.withRadiusAndColor(10, "Blue")

print(c1)
print(c2)
print(c3)