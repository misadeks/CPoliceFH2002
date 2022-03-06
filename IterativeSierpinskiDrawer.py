import turtle
import math

from util import get_random_color


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    @staticmethod
    def midpoint(pos1, pos2):
        return Position((pos1.x + pos2.x) // 2, (pos1.y + pos2.y) // 2)


class Triangle:
    def __init__(self, bottom_left_v, bottom_right, top_v):
        self.bottom_left_v = bottom_left_v
        self.bottom_right_v = bottom_right
        self.top_v = top_v

    def get(self):
        return self.bottom_left_v, self.bottom_right_v, self.top_v

    def draw(self, color="white"):
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

"""
    mode 0 - black & white
    mode 1 - 3 colors
    mode 2 - 4 colors
    mode 3 - 5 random colors, mode 1
    mode 4 - 5 random colors, mode 2
"""
class IterativeSierpinksiDrawer:
    def __init__(self, screen, size, position, mode):
        self.screen = screen
        self.size = size
        self.position = Position(*position)
        self.level = 0
        self.triangles = []
        self.mode = mode
        if mode == 1:
            # ovo je kada se u random color prosledjuje index
            self.colors = ["yellow", "orange", "red"]
        elif mode == 2:
            # ovaj ide ako se u random_color prosledi current_level
            self.colors = ["lime", "yellow", "orange", "red"]
        elif mode in (3, 4):
            self.colors = [get_random_color() for i in range(5)]
        turtle.tracer(0, 0)
        turtle.colormode(255)

    def draw_all(self, color="white"):
        for triangle in self.triangles:
            triangle.draw(color)

    @staticmethod
    def make_triangle(size, position):
        h = math.floor(size * math.sqrt(3) / 2)
        bottom_left_vertex = Position(position.x - size / 2, position.y - h // 3)
        bottom_right_vertex = Position(position.x + size / 2, position.y - h // 3)
        top_vertex = Position(position.x, position.y + 2 * h // 3)
        return Triangle(bottom_left_vertex, bottom_right_vertex, top_vertex)

    def pick_color(self, index):
        v = 0
        if self.mode in (1, 3):
            v = index
        elif self.mode in (2, 4):
            v = self.level
        return self.colors[v % len(self.colors)]

    def draw_next(self):
        if self.level == 0:
            self.triangles.append(self.make_triangle(self.size, self.position))
            self.draw_all("black")
        else:
            new_triangles = []
            index = 0
            for triangle in self.triangles:
                bottom_left_v, bottom_right_v, top_v = triangle.get()
                bottom_center_v = Position.midpoint(bottom_left_v, bottom_right_v)
                left_center_v = Position.midpoint(bottom_left_v, top_v)
                right_center_v = Position.midpoint(top_v, bottom_right_v)
                new_triangles.append(Triangle(bottom_left_v, bottom_center_v, left_center_v))
                new_triangles.append(Triangle(bottom_center_v, bottom_right_v, right_center_v))
                new_triangles.append(Triangle(left_center_v, right_center_v, top_v))
                if self.mode in range(1, 5):
                    # color modes
                    Triangle(left_center_v, right_center_v, bottom_center_v).draw(self.pick_color(index))
                    index += 1
                else:
                    Triangle(left_center_v, right_center_v, bottom_center_v).draw() # black-white

            self.triangles = new_triangles
        self.level += 1
