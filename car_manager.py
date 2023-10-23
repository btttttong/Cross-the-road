import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.counter = 0
        self.cars = []
        self.cars.append(self.create_car())
        # self.car_hit =

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.goto(300, random.randrange(-250, 250))
        self.cars.append(car)
        return car

    def car_move(self):
        self.counter += 1
        if self.counter % 6 == 0:
            self.create_car()
        for i in range(len(self.cars)):
            self.cars[i].setheading(180)
            self.cars[i].forward(MOVE_INCREMENT)


    def car_hit(self, player_pos):
        for i in range(len(self.cars)):
            if self.cars[i].distance(player_pos) < 20:
                return True

