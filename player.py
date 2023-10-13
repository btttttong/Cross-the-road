from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.color('green')
        self.set_start()

    def go_up(self):
        if self.ycor() <= FINISH_LINE_Y:
            y = self.ycor()
            y += MOVE_DISTANCE
            self.sety(y)

    def set_start(self):
        self.goto(STARTING_POSITION)
