from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Road")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
            
      
    if player.ycor() > player.finish:
        player.reset_position()
        scoreboard.level_up()
        car_manager.increase_move_speed()
        
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    
screen.exitonclick()