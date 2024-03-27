import time
import turtle
from turtle import *
from ball import Ball
from bricks import Bricks
from paddle import Paddle, screen
from score import Score


screen.setup(width=900, height=550)
screen.bgcolor('#C6EBC5')
screen.title("BreakOut Game")
screen.tracer(0)

ball = Ball()
paddle = Paddle()


def breakout_game():
    brick = Bricks()
    score = Score()
    score.retrieve_highest_score()

    # Asks users of the difficulty level and acts accordingly, defaults to "Easy" if no user input
    difficulty_level = numinput("Difficulty Level", "Enter 1 for Easy\n2 for Normal\n3 for Hard")
    if difficulty_level is not None:
        if difficulty_level == 1:
            ball.moving_distance = 7
        elif difficulty_level == 2:
            ball.moving_distance = 12
        elif difficulty_level == 3:
            ball.moving_distance = 17

    game_is_on = True
    while game_is_on:
        # Clears the old score and writes the current score on the screen
        score.clear()
        score.write(f"Score: {score.score} | Highest score: {score.highest_score}", align="center", font=("Arial", 12, "bold"))

        # Updates the screen after the game is set up
        screen.update()

        # Detecting ball collision with the walls
        if ball.xcor() <= -430 or ball.xcor() >= 430:
            ball.setheading(180 - ball.heading())
            ball.move()
        elif ball.ycor() >= 260:
            ball.setheading(-ball.heading())
            ball.move()
        else:
            ball.move()

        # Detecting ball collision with the bricks up
        for blocks in brick.brick:
            if abs(ball.ycor() - blocks.ycor()) < 15 and abs(ball.xcor() - blocks.xcor()) < 32:
                ball.setheading(-ball.heading())
                ball.move()
                blocks.goto(x=1000, y=1000)
                score.score += 1

        # Detecting ball collision with the paddle below
        if abs(ball.ycor() - paddle.ycor()) < 15 and abs(ball.xcor() - paddle.xcor()) < 40:
            ball.setheading(-ball.heading())

        # Detects when the paddle misses the ball and ends the game
        if ball.ycor() <= -260:
            paddle.resset()
            ball.resset()
            score.update_highest_score()
            game_is_on = False
            score.score = 0
            time.sleep(1)
            play_again = textinput("Play Again", "Do you wish to play again?\nEnter 'y' for Yes\nOR\nEnter 'n' for No")
            if play_again == 'y':
                score.clear()
                brick.resset()
                breakout_game()
            else:
                turtle.bye()

        # Link Mouse movements to the paddle movement
        turtle.listen()
        paddle.run_drag()

    # Increases the speed gradually after each 10 points
    # if score % 10 == 0:
    #     ball.moving_distance += 1


breakout_game()
screen.exitonclick()
