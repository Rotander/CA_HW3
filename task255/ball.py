import math

# ----------------------------------------------
import random


def read(ball, str_array, i):
    if i >= len(str_array) - 1:
        return 0
    ball.append("ball")
    ball.append(int(str_array[i]))  # плотность
    ball.append(int(str_array[i + 1]))  # радиус
    i += 2
    return i


def read_random(ball):
    ball.append("ball")
    ball.append(random.randint(1, 10))  # плотность
    ball.append(random.randint(1, 10))  # радиус


def write(ball, ostream):
    ostream.write("Ball: density = {}  r = {}, Volume = {}".format(ball[1], ball[2], volume(ball)))
    pass


def volume(ball):
    return 4.0 / 3 * math.pi * ball[2] * ball[2]
    pass
