from pyautogui import position


def position_generator():
    yield position()


def beeper():
    mouse_coords = next(position_generator())
    if mouse_coords == (0, 0):
        print('\a', end='')
    else:
        pass

def main():
    beeper()


if __name__ == '__main__':
    main()
