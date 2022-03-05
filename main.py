import turtle
import math
import time


def draw_sierpinski(size: int, iteration: int, x: int, y: int):
    color = "black" if iteration == 0 else "white"
    if iteration >= 0:
        draw_triangle(size, x, y, color)
        draw_sierpinski(int(size / 2), iteration - 1, *top_starting_point(int(size), x, y))
        draw_sierpinski(int(size / 2), iteration - 1, x, y)
        draw_sierpinski(int(size / 2), iteration - 1, x + int(size / 2), y)


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
    x_top = x + (size / 4)
    y_top = y + (size / 2) * math.sqrt(3) / 2
    return int(x_top), int(y_top)


def main():
    try:
        screen = turtle.Screen()
        turtle.tracer(0, 0)
        for i in range(8):
            screen.title(f"Sierpiński triangle - generation {i}")
            draw_sierpinski(800, i, -400, -320)
            turtle.update()
            time.sleep(1.25)8
        turtle.done()
    except turtle.Terminator:
        pass


if __name__ == '__main__':
    main()
