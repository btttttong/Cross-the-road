import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

car_speed = 0.1
game_is_on = True

while game_is_on:
    time.sleep(car_speed)
    screen.update()
    score.show_score()

    car.car_move()
    if car.car_hit(player.pos()):
        score.game_over()
        break

    if player.ycor() > 280:
        score.add_score()
        player.set_start()
        if car_speed > 0.001:
            car_speed -= 0.001

screen.mainloop()