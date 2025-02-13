# Problem 3: Draw a user-defined polygon
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program asks the user for polygon details and draws it using turtle.

import turtle

# Get user input
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Setup turtle
t = turtle.Turtle()
t.color(line_color)
t.fillcolor(fill_color)
t.begin_fill()

# Draw polygon
for _ in range(sides):
    t.forward(length)
    t.left(360 / sides)

t.end_fill()
turtle.done()
