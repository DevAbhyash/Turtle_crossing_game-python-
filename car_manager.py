from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITION =[(230,30),(230,25),(230,20),(230,10),(230,0),(230,-10)]
starting_move_distance = 5
move_increment = 10


class CarManager(Turtle):
    def __init__(self):
      self.all_cars=[]
      self.car_speed = starting_move_distance

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
         new_car = Turtle("square")
         new_car.shapesize(stretch_wid=1,stretch_len=2)
         new_car.penup()
         new_car.color(random.choice(COLORS))
         random_y = random.randint(-250,250)
         new_car.goto(300,random_y)
         self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=move_increment


