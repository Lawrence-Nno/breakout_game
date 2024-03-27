import turtle
from turtle import *
from turtle import Turtle

screen = Screen()


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.x = -0
        self.y = -250
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.goto(x=self.x, y=self.y)
        self.moving_distance = 40

    def move_right(self):
        self.forward(self.moving_distance)
        screen.update()

    def move_left(self):
        self.backward(self.moving_distance)
        screen.update()

    def resset(self):
        self.clear()
        self.goto(x=self.x, y=self.y)
        screen.update()

    def dragging(self, x, y=-250.0):  # These parameters will be the mouse position
        self.ondrag(None)
        self.setheading(self.towards(x, y=-250.0))
        self.goto(x, y=-250.0)
        self.ondrag(self.dragging)

    def run_drag(self):
        turtle.listen()
        self.ondrag(self.dragging)
