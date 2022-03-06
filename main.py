import time

from util import get_window_size
from IterativeSierpinskiDrawer import *


def get_origin_position(size):
    return 0, -size // 8


def main():
    screen = turtle.Screen()
    size = get_window_size()
    position = get_origin_position(size)
    drawer = IterativeSierpinksiDrawer(screen, size, position, 4)

    for i in range(8):
        screen.title(f"Sierpiński triangle - {i}. iteration")
        drawer.draw_next()
        turtle.update()
        time.sleep(0.75)
    turtle.done()


if __name__ == '__main__':
    try:
        main()
    except turtle.Terminator:
        exit(0)
