from turtle import Turtle
import os


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        self.score = 0
        self.highest_score = 0
        self.file_path = "highest_score.txt"

    def retrieve_highest_score(self):
        if os.path.exists(self.file_path):
            with open(file=self.file_path, mode='r') as file:
                self.highest_score = file.read()

    def update_highest_score(self):
        if not os.path.exists(self.file_path):
            with open(file="highest_score.txt", mode="w") as f:
                f.write(f"{self.score}")
        else:
            with open(file=self.file_path, mode="r+") as f:
                self.highest_score = f.read()
                if self.score > int(self.highest_score):
                    with open(file=self.file_path, mode="w") as file:
                        file.write(f"{self.score}")