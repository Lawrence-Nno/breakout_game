from turtle import Turtle


NUM_OF_TURTLES_PER_SLIDE = 1
NUM_OF_TURTLE_PER_ROW = 13
NUM_OF_ROWS = 6
TOTAL_NUM_OF_TURTLE = NUM_OF_TURTLE_PER_ROW * NUM_OF_ROWS


# def create_bricks():
#     brick = []
#     x = -290
#     y = 200
#     turtle_per_slide_tracker = 1
#     turtle_per_row_tracker = 1
#     color_list = ['red', 'orange', 'pink', 'yellow', 'sky blue', 'green']
#     color_num = 0
#     for _ in range(TOTAL_NUM_OF_TURTLE):
#         brick.append(Turtle('square'))
#         brick[_].shapesize(stretch_wid=0.5, stretch_len=1)
#         brick[_].color(color_list[color_num])
#         brick[_].penup()
#         brick[_].speed("fastest")
#         brick[_].goto(x=x, y=y)
#
#         if turtle_per_slide_tracker % NUM_OF_TURTLES_PER_SLIDE != 0:
#             x += 21
#         else:
#             x += 23
#         turtle_per_slide_tracker += 1
#         if turtle_per_row_tracker % NUM_OF_TURTLE_PER_ROW != 0:
#             y += 0
#         else:
#             color_num += 1
#             x = -290
#             y -= 13
#         turtle_per_row_tracker += 1


class Bricks(Turtle):
    def __init__(self):
        self.brick = []
        self.x = -390
        self.y = 230
        self.turtle_per_slide_tracker = 1
        self.turtle_per_row_tracker = 1
        self.color_list = ['red', 'orange', 'pink', 'yellow', 'sky blue', 'green']
        self.color_num = 0

        # def create_bricks():
        for _ in range(TOTAL_NUM_OF_TURTLE):
            self.brick.append(Turtle('square'))
            self.brick[_].shapesize(stretch_wid=0.5, stretch_len=3)
            self.brick[_].color(self.color_list[self.color_num])
            self.brick[_].penup()
            self.brick[_].speed("fastest")
            self.brick[_].goto(x=self.x, y=self.y)
            self.x += 65
            if self.turtle_per_row_tracker % NUM_OF_TURTLE_PER_ROW == 0:
                self.color_num += 1
                self.x = -390
                self.y -= 13
            self.turtle_per_row_tracker += 1

    def resset(self):
        for seg in self.brick:
            seg.reset()
            seg.penup()
            seg.goto(1000, 1000)