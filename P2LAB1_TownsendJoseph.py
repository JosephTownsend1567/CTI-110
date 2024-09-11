# Joseph Townsend
# 9/11/2024
# P2LAB1
# Calculate math related to a circle

#imports the math library
import math

# Get float input from user (radius)
radius = float(input("What is the radius of the circle? "))
print()
#calculates the diameter
diameter = radius * 2
print("The diameter of the circle is", diameter)

#calculates the circumference
circumference = 2 * math.pi * radius
print("The circumference is of the ciricle is", round(circumference, 2))

#calculate the area
area = math.pi * (radius ** 2)
print("The area is of the ciricle is", round(area, 3))
