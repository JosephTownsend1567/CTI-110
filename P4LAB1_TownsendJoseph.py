# Joseph Townsend
# 9/23/2024
# P4LAB1
# Use turtle library to draw shapes with loops

#Import the turtle library for drawing
import turtle

#create a window for turtle to draw in (executable)
window = turtle.Screen()

#create a turtle object
bennett = turtle.Turtle()

# For loop to draw a square
for side in range(4):
    bennett.forward(150)
    bennett.right(90)
    
# while loop to draw a triangle
var = 0
while var < 3:
    bennett.forward(150)
    bennett.left(120)
    var = var + 1
print("Loop is broken, var is at", var)

    
