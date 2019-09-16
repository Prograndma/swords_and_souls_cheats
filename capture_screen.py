import numpy as np
from PIL import ImageGrab
import math
from time import sleep
from pykeyboard import PyKeyboard
from key_press_thread import Press
from PIL import Image


game_cords = [122, 121, 925, 724]     # There must be two pixels outside of the game screen for this to work best.

up_pixel = 125
right_pixel = 105
down_pixel = 100
left_pixel = 135

keyboard = PyKeyboard()


top_apple_bbox = (int((387 / 803) * (game_cords[2] - game_cords[0])),
                  int((210 / 603) * (game_cords[3] - game_cords[1])),
                  int((412 / 803) * (game_cords[2] - game_cords[0])),
                  int((240 / 603) * (game_cords[3] - game_cords[1])))

middle_apple_bbox = (int((387 / 803) * (game_cords[2] - game_cords[0])),
                     int((340 / 603) * (game_cords[3] - game_cords[1])),
                     int((412 / 803) * (game_cords[2] - game_cords[0])),
                     int((370 / 603) * (game_cords[3] - game_cords[1])))

bottom_apple_bbox = (int((387 / 803) * (game_cords[2] - game_cords[0])),
                     int((418 / 603) * (game_cords[3] - game_cords[1])),
                     int((412 / 803) * (game_cords[2] - game_cords[0])),
                     int((450 / 603) * (game_cords[3] - game_cords[1])))

perfect_bbox = (int((40 / 803) * (game_cords[2] - game_cords[0])),
                int((80 / 603) * (game_cords[3] - game_cords[1])),
                int((60 / 803) * (game_cords[2] - game_cords[0])),
                int((100 / 603) * (game_cords[3] - game_cords[1])))


def find_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def average_of_box(array):
    return np.mean(array)


def check_up_press(screen):
    want = screen[top_apple_bbox[1]:top_apple_bbox[3], top_apple_bbox[0]:top_apple_bbox[2]]
    average = average_of_box(want)

    if average < up_pixel:
        Press(key=keyboard.up_key, delay=.37, keyboard=keyboard).start()
        return True
    return False


def check_right_press(screen):
    want = screen[middle_apple_bbox[1]:middle_apple_bbox[3], middle_apple_bbox[0]:middle_apple_bbox[2]]
    average = average_of_box(want)

    if average < right_pixel:
        Press(key=keyboard.right_key, delay=.35, keyboard=keyboard).start()
        return True
    return False


def check_down_press(screen):
    want = screen[bottom_apple_bbox[1]:bottom_apple_bbox[3], bottom_apple_bbox[0]:bottom_apple_bbox[2]]
    average = average_of_box(want)

    if average < down_pixel:
        Press(key=keyboard.down_key, delay=.35, keyboard=keyboard).start()
        return True
    return False


def check_left_press(screen):
    want = screen[perfect_bbox[1]:perfect_bbox[3], perfect_bbox[0]:perfect_bbox[2]]
    average = average_of_box(want)

    if average > left_pixel:
        Press(key=keyboard.left_key, delay=.55, keyboard=keyboard).start()
        return True
    return False


if __name__ == "__main__":

    sleep(2)

    up = False
    down = False
    left = False
    right = False
    up_counter = 0
    down_counter = 0
    left_counter = 0
    right_counter = 0
    normal_limit = 6

    special_limit = 3
    while True:

        screen_red = np.array(ImageGrab.grab(bbox=game_cords))[:, :, 1]

        if not up:
            up = check_up_press(screen_red)
        else:
            up_counter += 1
            if up_counter > normal_limit:
                up = False
                up_counter = 0
        if not right:
            right = check_right_press(screen_red)
        else:
            right_counter += 1
            if right_counter > normal_limit:
                right = False
                right_counter = 0
        if not down:
            down = check_down_press(screen_red)
        else:
            down_counter += 1
            if down_counter > normal_limit:
                down = False
                down_counter = 0
        if not left:
            left = check_left_press(screen_red)
        else:
            left_counter += 1
            if left_counter > special_limit:
                left = False
                left_counter = 0


# for x in range(int((387/803) * (game_cords[2] - game_cords[0])),
#                int((412/803) * (game_cords[2] - game_cords[0]))):
#     for y in range(int((210 / 603) * (game_cords[3] - game_cords[1])),
#                    int((240 / 603) * (game_cords[3] - game_cords[1]))):
#         real_screen.putpixel((x, y), (255, 255, 255))


# for x in range(int((387/803) * (game_cords[2] - game_cords[0])),
#                int((412/803) * (game_cords[2] - game_cords[0]))):
#     for y in range(int((340 / 603) * (game_cords[3] - game_cords[1])),
#                    int((370 / 603) * (game_cords[3] - game_cords[1]))):
#         real_screen.putpixel((x, y), (255, 255, 255))

# for x in range(int((387/803) * (game_cords[2] - game_cords[0])),
#                int((412/803) * (game_cords[2] - game_cords[0]))):
#     for y in range(int((418 / 603) * (game_cords[3] - game_cords[1])),
#                    int((450 / 603) * (game_cords[3] - game_cords[1]))):
#         real_screen.putpixel((x, y), (255, 255, 255))

# for x in range(int((40/803) * (game_cords[2] - game_cords[0])),
#                int((60/803) * (game_cords[2] - game_cords[0]))):
#     for y in range(int((80 / 603) * (game_cords[3] - game_cords[1])),
#                    int((100 / 603) * (game_cords[3] - game_cords[1]))):
#         real_screen.putpixel((x, y), (255, 255, 255))

# real_screen.show()