import pandas as pd
import turtle

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

correct_guess = []

data = pd.read_csv("50_states.csv")

game_is_on = True

while game_is_on:
    anwser_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name?").lower().title()
    if len(correct_guess) < 50:
        if anwser_state == "Exit":
            missing_states = [state for state in data.state.values if state not in correct_guess]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break    
        elif anwser_state in data.state.values and anwser_state not in correct_guess:
            correct_guess.append(anwser_state)
            coordinates = data[data.state == anwser_state].values.tolist()[0][1:]
            
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(coordinates[0], coordinates[1])
            t.write(anwser_state, align="right")
    else:
        game_is_on = False
    

