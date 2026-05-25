pi = 3.141592653589793
radius = float(input("Enter the radius of the circle: "))
angle = float(input("Enter the angle in degrees: "))
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius
sector_area = (angle / 360) * area
arc_length = (angle / 360) * circumference
print("Radius:", radius)
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Sector Area for", angle, "degrees:", sector_area)
print("Arc Length for", angle, "degrees:", arc_length)