import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scores import Scores

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scores()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collisions
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #for successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()



screen.exitonclick()