import time

from util import get_window_size, ConsoleColors
from IterativeSierpinskiDrawer import *


def get_origin_position(size):
    return 0, -size // 8


def main():
    print(f"{ConsoleColors.HEADER}TROUGAO SJERPINSKOG{ConsoleColors.ENDC}")

    try:
        generation_number = int(input(
            f"{ConsoleColors.BOLD}Uneti broj generacija (podrazumevano "
            f"{ConsoleColors.OKBLUE}6{ConsoleColors.ENDC}{ConsoleColors.BOLD}): {ConsoleColors.ENDC}"))
    except:
        print(f"{ConsoleColors.WARNING}Korišćena je podrazumevana vrednost {ConsoleColors.OKBLUE}6{ConsoleColors.ENDC}")
        generation_number = 6

    print(f"""Načini crtanja su sledeći:
{ConsoleColors.OKBLUE}0. crno-belo (klasični){ConsoleColors.ENDC}
1. 3 boje (predefinisane)
2. 4 boje (predefinisane)
3. 3 boje (nasumične)
4. 4 boje (nasumične)""")

    try:
        option = int(input(
            f"{ConsoleColors.BOLD}Uneti redni broj ispred željenje opcije (podrazumevano "
            f"{ConsoleColors.OKBLUE}0{ConsoleColors.ENDC}{ConsoleColors.BOLD}): {ConsoleColors.ENDC}"))
    except:
        print(f"{ConsoleColors.WARNING}Korišćena je podrazumevana vrednost {ConsoleColors.OKBLUE}0{ConsoleColors.ENDC}")
        option = 0

    screen = turtle.Screen()
    size = get_window_size()
    position = get_origin_position(size)
    drawer = IterativeSierpinksiDrawer(screen, size, position, option)

    print(f"{ConsoleColors.OKGREEN}Crtanje započeto!{ConsoleColors.ENDC}")
    for i in range(generation_number + 1):
        screen.title(f"Trougao Sjerpinskog - {i}. generacija")
        drawer.draw_next()
        turtle.update()
        time.sleep(0.75)
    turtle.done()


if __name__ == '__main__':
    try:
        main()
    except turtle.Terminator:
        exit(0)
