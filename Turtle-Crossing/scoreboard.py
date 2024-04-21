from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f'Level {self.level}', align='center', font=FONT)

    def increase_level(self):
        self.level += 1


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
