from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food= Food()
scoreboard= ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision detection
    if snake.head.distance(food)<15 :
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segments in snake.segments[1: ]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            scoreboard.game_over()












screen.exitonclick()
