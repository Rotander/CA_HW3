# ----------------------------------------------
import random
from math import sqrt


def read(tetrahedron, str_array, i):
    if i >= len(str_array) - 1:
        return 0
    tetrahedron.append("tetrahedron")
    tetrahedron.append(int(str_array[i]))  # плотность
    tetrahedron.append(int(str_array[i + 1]))  # длина ребра
    i += 2
    return i


def read_random(tetrahedron):
    tetrahedron.append("tetrahedron")
    tetrahedron.append(random.randint(1, 10))  # плотность
    tetrahedron.append(random.randint(1, 10))  # длина ребра


def write(tetrahedron, ostream):
    ostream.write(
        "Tetrahedron: density = {}  a = {}, Volume = {}".format(tetrahedron[1], tetrahedron[2], volume(tetrahedron)))
    pass


def volume(tetrahedron):
    return tetrahedron[2] * tetrahedron[2] * tetrahedron[2] * sqrt(2) / 12
    pass
