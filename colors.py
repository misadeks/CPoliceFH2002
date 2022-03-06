import random

Color = tuple[int, int, int]


class Colors:
    """This class has methods for generating colors"""
    @staticmethod
    def random() -> Color:
        """This method generates a new color in rgb color system"""
        num = random.randint(0, 2**24)
        r = (num & 0xff0000) >> 16
        g = (num & 0x00ff00) >> 8
        b = num & 0x0000ff
        return r, g, b

    @staticmethod
    def random_pallet(size: int) -> list[Color]:
        """This method generates a list of several rgb colors"""
        return [Colors.random() for i in range(size)]
