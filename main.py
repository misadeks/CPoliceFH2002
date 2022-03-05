import turtle
import math
import time

from stack import *


def get_screen_resolution():
    import tkinter as tk
    (root := tk.Tk()).withdraw()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height


def get_window_size():
    resolution = get_screen_resolution()
    min_dimension = min(resolution[0], resolution[1])
    return int(0.75 * (min_dimension / 100) * 100)


def get_color(iter):
    return "black" if iter == 0 else "white"


def draw_sierpinski(size: int, iteration: int, x: int, y: int):
    s = Stack()
    s.push((size, iteration, x, y))
    while not s.empty():
        size, level, x, y = s.take()
        if level >= 0:
            draw_triangle(size, x, y, get_color(level))
            s.push((size // 2, level - 1, x + size//2, y))
            s.push((size // 2, level - 1, x, y))
            s.push((size // 2, level - 1, *top_starting_point(size, x, y)))


def draw_triangle(size: int, x: int, y: int, color):
    t = turtle.Turtle(visible=False)
    t.fillcolor(color)
    t.speed(0)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.end_fill()


def top_starting_point(size: int, x: int, y: int):
    x_top = x + size // 4
    y_top = y + size * math.sqrt(3) / 4
    return x_top, math.floor(y_top)


def main():
    screen = turtle.Screen()
    turtle.tracer(0, 0)
    size = get_window_size()
    for i in range(8):
        screen.title(f"Sierpiński triangle - {i}. iteration")
        draw_sierpinski(size, i, -size // 2, -int(size * 0.4))
        turtle.update()
        time.sleep(1.25)
    turtle.done()


if __name__ == '__main__':
    try:
        main()
    except turtle.Terminator:
        exit(0)
