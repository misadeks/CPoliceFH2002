import turtle
import math

iteration = 0


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


def draw_sierpinski(size: int, iteration: int, x: int, y: int):
    color = "black" if iteration == 1 else "white"
    if iteration:
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


def one_step():
    global iteration
    print(iteration)
    # screen.title(f"Sierpiński triangle - generation {iteration}")
    size = get_window_size()
    draw_sierpinski(size, iteration, -size // 2, -int(size*0.4))
    iteration += 1
    turtle.update()
    if iteration < 7:
        turtle.ontimer(one_step, 1250)
    else:
        turtle.done()


def main():
    screen = turtle.Screen()
    screen.title(f"Sierpiński triangle")
    turtle.tracer(0, 0)
    one_step()
    screen.mainloop()


if __name__ == '__main__':
    main()