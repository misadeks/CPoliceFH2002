import turtle
from position import *


class Triangle:
    def __init__(self, bottom_left_v: Position, bottom_right: Position, top_v: Position):
        self.bottom_left_v = bottom_left_v
        self.bottom_right_v = bottom_right
        self.top_v = top_v

    def get(self):
        return self.bottom_left_v, self.bottom_right_v, self.top_v

    def base_midpoint(self):
        return Position.midpoint(self.bottom_left_v, self.bottom_right_v)

    def left_side_midpoint(self):
        return Position.midpoint(self.bottom_left_v, self.top_v)

    def right_size_midpoint(self):
        return Position.midpoint(self.top_v, self.bottom_right_v)

    def draw(self, color: str = "white"):
        t = turtle.Turtle(visible=False)
        t.fillcolor(color)
        t.speed(0)
        t.up()
        t.goto(*self.bottom_left_v.get())
        t.down()
        t.begin_fill()
        t.goto(*self.bottom_right_v.get())
        t.goto(*self.top_v.get())
        t.goto(*self.bottom_left_v.get())
        t.end_fill()
