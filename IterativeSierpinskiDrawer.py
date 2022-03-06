import math
from colors import Colors
from triangle import *


class IterativeSierpinksiDrawer:
    """
        This class draws Sierpinski Triangle in increments on the turtle canvas.
        Triangle is centered at the position passed to the constructor, and it can be drawn in several modes,
        based on the provided argument;
            mode=0 - black & white
            mode=1 - 3 colors
            mode=2 - 4 colors
            mode=3 - 3 random colors, similar to mode 1
            mode=4 - 3 random colors, similar to mode 2
    """
    def __init__(self, screen: type(turtle.Screen()), size: int, position: Position, mode: int):
        self.screen = screen
        self.size = size
        self.position = position
        self.level = 0
        self.triangles = []
        self.mode = mode
        if mode == 1:
            self.colors = ["yellow", "orange", "red"]
        elif mode == 2:
            self.colors = ["lime", "yellow", "orange", "red"]
        elif mode in (3, 4):
            self.colors = Colors.random_pallet(mode)
        turtle.tracer(0, 0)
        turtle.colormode(255)

    def __pick_color(self, index: int) -> str | tuple[int, int, int]:
        """Depending on the drawing mode, picks the color for the next layer"""
        ind = 0
        if self.mode in (1, 3):
            ind = index
        elif self.mode in (2, 4):
            ind = self.level
        return self.colors[ind % len(self.colors)]

    def draw_next(self) -> None:
        """Calculates triangles to be drawn in order to create a new layer, then draws them"""
        if self.level == 0:
            # If first layer is being drawn, only draw an centered empty black triangle
            x, y = self.position.get()
            h = math.floor(self.size * math.sqrt(3) / 2)
            bottom_left_vertex = Position(x - self.size // 2, y - h // 3)
            bottom_right_vertex = Position(x + self.size // 2, y - h // 3)
            top_vertex = Position(x, y + 2 * h // 3)
            self.triangles.append(Triangle(bottom_left_vertex, bottom_right_vertex, top_vertex))
            self.triangles[0].draw("black")
        else:
            """For all other layers, new triangles should be generated
            In each iteration one of triangles from previous layer is split in 4 parts,
            and the middle part is deleted, while others are returned into the array"""
            new_triangles = []
            index = 0
            for triangle in self.triangles:
                bottom_left_v, bottom_right_v, top_v = triangle.get()
                # First generate midpoints of all the sides of the triangle
                bottom_center_v = triangle.base_midpoint()
                left_center_v = triangle.left_side_midpoint()
                right_center_v = triangle.right_size_midpoint()
                # Create small triangles that are bottom left, bottom right and top parts of the original
                new_triangles.append(Triangle(bottom_left_v, bottom_center_v, left_center_v))
                new_triangles.append(Triangle(bottom_center_v, bottom_right_v, right_center_v))
                new_triangles.append(Triangle(left_center_v, right_center_v, top_v))
                # Based on color mode, color the inner part of the current triangle ( delete it)
                if self.mode in range(1, 5):
                    # If triangle is drawn in color
                    Triangle(left_center_v, right_center_v, bottom_center_v).draw(self.__pick_color(index))
                    index += 1
                else:
                    # If triangle is black and white
                    Triangle(left_center_v, right_center_v, bottom_center_v).draw()

            # Replace old triangles
            self.triangles = new_triangles
        self.level += 1
