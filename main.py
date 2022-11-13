import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.onkey(player.move_up,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #DETECT COLLISION
    for car in car_manager.all_cars:
       if car.distance(player)<20:
         game_is_on=False
         score.game_over()
    #DETECT SUCESSFULL CROSSING
    if player.ycor()>300:
        player.completed_round()
        car_manager.level_up()
        score.increase_score()

screen.exitonclick()
