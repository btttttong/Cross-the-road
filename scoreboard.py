from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()

    def show_score(self):
        self.clear()
        self.speed(0)
        self.hideturtle()
        self.goto(0, 260)
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!!!!!!!!', align='center', font=FONT)

    def add_score(self):
        self.score += 1
