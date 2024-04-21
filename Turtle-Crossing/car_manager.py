from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.move_increase = 0
        self.generate_car()

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.move_increase)

    def generate_car(self):
        random_y = random.randint(-250, 250)
        random_color = random.choice(COLORS)
        self.color(random_color)
        self.goto(320, random_y)

    def increase_difficulty(self, level):
        self.clear()
        self.move_increase = MOVE_INCREMENT * level


