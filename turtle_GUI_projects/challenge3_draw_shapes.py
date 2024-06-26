from turtle import Turtle, Screen
import random

tim = Turtle()

# # Challange 3: Drawing different Shapes
def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.color(r,g,b)

def draw_shape(angles):
    for j in range(angles):
        tim.forward(100)
        tim.right(360/angles)

for number_of_angles in range(3,11):
    change_color()
    draw_shape(number_of_angles)


screen = Screen()
screen.exitonclick()