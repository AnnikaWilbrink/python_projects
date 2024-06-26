from turtle import Turtle, Screen
import random

tim = Turtle()


# # Challenge 4: Generate a Random Walk
def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.color(r,g,b)

directions = [0,90,180,270]
tim.pensize(10)
tim.speed(20)
for i in range(200):
    change_color()
    tim.forward(15)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()