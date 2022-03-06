resolution_cached = False
resolution_cache = None


def screen_resolution():
    """This method gets the size of the users screen in pixels"""
    global resolution_cache, resolution_cached
    if not resolution_cached:
        import tkinter as tk
        (root := tk.Tk()).withdraw()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        resolution_cached = True
        resolution_cache = screen_width, screen_height

    return resolution_cache


def window_size() -> int:
    """This method calculates optimal size of the window, based on user's screen"""
    resolution = screen_resolution()
    min_dimension = min(resolution[0], resolution[1])
    return int(0.75 * (min_dimension / 100) * 100)


class ConsoleColors:
    """This class holds color values for the console output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'