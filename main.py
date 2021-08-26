import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)


def new_game():
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)  # turn off screen auto refresh

    score = Scoreboard()
    food = Food()
    snake = Snake()

    screen.listen()
    screen.onkeypress(snake.change_snake_direction_up, "Up")
    screen.onkeypress(snake.change_snake_direction_down, "Down")
    screen.onkeypress(snake.change_snake_direction_left, "Left")
    screen.onkeypress(snake.change_snake_direction_right, "Right")
    screen.onkey(restart_game, "R".lower())

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()

        # detect when snake get food
        if snake.snake_head.distance(food) < 15:
            food.refresh_position()
            snake.extend_snake()
            score.change_score()

        # detect when snake hits the wall
        if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
            game_is_on = False
            score.game_over()

        # detect when snake hits yor body
        for snake_part in snake.snake_body[1:]:
            if snake.snake_head.distance(snake_part) < 10:
                game_is_on = False
                score.game_over()

    screen.exitonclick()


def restart_game():
    screen.clearscreen()
    new_game()


new_game()
