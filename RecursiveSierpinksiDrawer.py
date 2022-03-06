import turtle
import math

from stack import *


class RecursiveSierpinksiDrawer:
    def __init__(self, screen, size, position):
        self.screen = screen
        self.size = size
        self.position = position
        self.currentLevel = 0
        turtle.tracer(0, 0)

    @staticmethod
    def get_color(level):
        return "black" if level == 0 else "white"

    @staticmethod
    def top_starting_point(t_size: int, x: int, y: int):
        x_top = x + t_size // 4
        y_top = y + t_size * math.sqrt(3) / 4
        return x_top, math.floor(y_top)

    @staticmethod
    def draw_triangle(t_size: int, x: int, y: int, lvl):
        t = turtle.Turtle(visible=False)
        t.fillcolor(RecursiveSierpinksiDrawer.get_color(lvl))
        t.speed(0)
        t.up()
        t.goto(x, y)
        t.down()
        t.begin_fill()
        t.forward(t_size)
        t.left(120)
        t.forward(t_size)
        t.left(120)
        t.forward(t_size)
        t.end_fill()

    def draw_next(self):
        s = Stack()
        s.push((self.size, self.position, self.currentLevel))
        while not s.empty():
            ssize, pos, lvl = s.take()
            px, py = pos
            if lvl >= 0:
                RecursiveSierpinksiDrawer.draw_triangle(ssize, px, py, lvl)
                s.push((ssize // 2, (px + ssize // 2, py), lvl - 1))
                s.push((ssize // 2, (px, py), lvl - 1))
                s.push((ssize // 2, RecursiveSierpinksiDrawer.top_starting_point(ssize, px, py), lvl - 1))
        self.currentLevel += 1