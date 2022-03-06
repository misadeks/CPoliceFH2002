import random

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


def get_random_color():
    num = random.randint(0, 2**24)
    r = (num & 0xff0000) >> 16
    g = (num & 0x00ff00) >> 8
    b = num & 0x0000ff
    return r, g, b


class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'