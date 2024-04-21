import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')
all_cars = []

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key='Up')

game_is_on = True
start_time = time.time()
while game_is_on:
    time_difference = time.time() - start_time
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    if time_difference > 1 / scoreboard.level:
        random_car = CarManager()
        all_cars.append(random_car)
        start_time = time.time()

    for car in all_cars:
        car.move()

        if car.xcor() < -320:
            all_cars.remove(car)
            car.clear()

        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() > 280:
            scoreboard.increase_level()
            player.reset()

        car.increase_difficulty(scoreboard.level - 1)
screen.exitonclick()
