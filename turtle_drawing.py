# Problem 5: Draw a creative picture using turtle
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program uses turtle graphics to draw a colorful spiral.

import turtle
import random

# Setup turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Draw a spiral pattern
for i in range(100):
    t.pencolor(random.choice(colors))  # Random color
    t.forward(i * 2)  # Move forward
    t.left(59)  # Turn left

turtle.done()
