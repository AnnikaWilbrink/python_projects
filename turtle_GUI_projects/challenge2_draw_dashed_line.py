from turtle import Turtle, Screen
import random

tim = Turtle()

# # Challenge 2: Draw a dashed line
for x in range(15):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()


screen = Screen()
screen.exitonclick()