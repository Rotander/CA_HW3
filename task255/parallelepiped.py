# ----------------------------------------------
import random


def read(parallelepiped, str_array, i):
    if i >= len(str_array) - 3:
        return 0
    parallelepiped.append("parallelepiped")
    parallelepiped.append(int(str_array[i]))  # плотность
    parallelepiped.append(int(str_array[i + 1]))  # ребро a
    parallelepiped.append(int(str_array[i + 2]))  # ребро b
    parallelepiped.append(int(str_array[i + 3]))  # ребро c
    i += 4
    return i


def read_random(parallelepiped):
    parallelepiped.append("parallelepiped")
    parallelepiped.append(random.randint(1, 10))  # плотность
    parallelepiped.append(random.randint(1, 10))  # ребро a
    parallelepiped.append(random.randint(1, 10))  # ребро b
    parallelepiped.append(random.randint(1, 10))  # ребро c


def write(parallelepiped, ostream):
    ostream.write(
        "Parallelepiped: density = {}  a = {} b = {} c = {}, Volume = {}".format(parallelepiped[1], parallelepiped[2],
                                                                                 parallelepiped[3], parallelepiped[4],
                                                                                 volume(parallelepiped)))
    pass


def volume(rect):
    return rect[2] * rect[3] * rect[4]
    pass
