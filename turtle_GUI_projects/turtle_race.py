from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -70
all_turtles = []


if user_bet in colors:
    print(f"You've bet on {user_bet}")
    is_race_on = True
    for turtle_index in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230,y=y)
        y += 30
        all_turtles.append(new_turtle)
else:
    print("Incorrect bet")
    
 
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


# screen.exitonclick()