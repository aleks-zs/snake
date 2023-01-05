import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


BORDER_POSITIVE = 280
BORDER_NEGATIVE = -280


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.125)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # border collision
    if snake.head.xcor() > BORDER_POSITIVE or\
            snake.head.xcor() < BORDER_NEGATIVE or\
            snake.head.ycor() > BORDER_POSITIVE or\
            snake.head.ycor() < BORDER_NEGATIVE:
        game_on = False
        scoreboard.game_over()

    # tail collision
    for s in snake.body[1:]:
        if snake.head.distance(s) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
