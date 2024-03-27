import time
from turtle import *

screen = Screen()
# screen.bgcolor('#C6EBC5')
# screen.title("Breakball Game")
# screen.tracer(0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = -237
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(x=self.x, y=self.y)
        self.left(45)
        self.moving_distance = 7


    def move(self):
        self.forward(self.moving_distance)

    def resset(self):
        self.clear()
        self.penup()
        self.goto(x=self.x, y=self.y)
        self.setheading(45)
        screen.update()



# ball = Ball()
# ball.move()
# while True:
#     if ball.xcor() <= -300 or ball.xcor() >= 300 or ball.ycor() <= -300 or ball.ycor() >= 300:
#         ball.right(95)
#         ball.forward(20)
#     else:
#         ball.forward(20)

# screen.update()
# screen.exitonclick()