from turtle import Turtle, Screen
import random

tim = Turtle()

# Challenge 5: Draw a Spirograph
def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.color(r,g,b)

tim.speed(20)
for i in range(0, 361, 5):
    change_color()
    tim.circle(100)
    tim.setheading(i)

screen = Screen()
screen.exitonclick()