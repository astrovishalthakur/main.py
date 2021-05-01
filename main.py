from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# create snake
snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
# move snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    scoreboard.update()
    snake.move()
    # detecting collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inc_sc()
        scoreboard.update()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detecting collisions with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        else:
            pass

screen.exitonclick()
