# ----------------------------------------------
import random

from extender import *


def read(container_item, str_array):
    array_len = len(str_array)
    i = 0  # Индекс, задающий текущую строку в массиве
    fig_num = 0  # Счетчк фигур
    while i < array_len:
        str = str_array[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)    # тестовый вывод ключа фигуры
        if key == 1:  # признак шара
            i += 1
            ball_item = []  # шар - это список с признаком и значениями
            i = ball.read(ball_item, str_array, i)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(ball_item)  # шар поступает в контейнер
        elif key == 2:  # признак параллелепипеда
            i += 1
            parallelepiped_item = []  # параллелепипед - это список с признаком и значениями
            i = parallelepiped.read(parallelepiped_item, str_array,
                                    i)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(parallelepiped_item)  # параллелепипед поступает в контейнер
        elif key == 3:  # признак тетраэдра
            i += 1
            tetrahedron_item = []  # тетраэдр - это список с признаком и значениями
            i = tetrahedron.read(tetrahedron_item, str_array,
                                 i)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(tetrahedron_item)  # тетраэдр поступает в контейнер
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return fig_num
        # Количество фигур увеличивается на 1
        if i == 0:
            return fig_num
        fig_num += 1
    return fig_num


def random_generate(container_item, count):
    fig_num = 0  # Счетчк фигур
    for i in range(count):
        key = random.randint(1, 3)  # преобразование в целое
        if key == 1:  # признак шара
            ball_item = []  # шар - это список с признаком и значениями
            i = ball.read_random(ball_item)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(ball_item)  # шар поступает в контейнер
        elif key == 2:  # признак параллелепипеда
            parallelepiped_item = []  # параллелепипед - это список с признаком и значениями
            i = parallelepiped.read_random(
                parallelepiped_item)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(parallelepiped_item)  # параллелепипед поступает в контейнер
        elif key == 3:  # признак тетраэдра
            tetrahedron_item = []  # тетраэдр - это список с признаком и значениями
            i = tetrahedron.read_random(
                tetrahedron_item)  # Заполнение фигуры значением и получение следующей позиции
            container_item.append(tetrahedron_item)  # тетраэдр поступает в контейнер
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return fig_num
        # Количество фигур увеличивается на 1
        if i == 0:
            return fig_num
        fig_num += 1
    return fig_num


def write(cont, ostream):
    ostream.write("Container stores {} shapes:\n".format(len(cont)))
    for shape in cont:
        if shape[0] == "ball":
            ball.write(shape, ostream)
        elif shape[0] == "parallelepiped":
            parallelepiped.write(shape, ostream)
        elif shape[0] == "tetrahedron":
            tetrahedron.write(shape, ostream)
        else:
            ostream.write("Incorrect figure ")
            ostream.write(shape)
        ostream.write("\n")
    ostream.write("Summa of Volume  = {}\n".format(volume(cont)))
    pass


def volume(cont):
    volume_value = 0.0
    for shape in cont:
        if shape[0] == "ball":
            volume_value += ball.volume(shape)
        elif shape[0] == "parallelepiped":
            volume_value += parallelepiped.volume(shape)
        elif shape[0] == "tetrahedron":
            volume_value += tetrahedron.volume(shape)
        else:
            volume_value += 0.0
    return volume_value


def volume_filter(cont):
    volume_value = volume(cont) / len(cont)
    new_container = []
    for shape in cont:
        if shape[0] == "ball" and ball.volume(shape) >= volume_value or \
                shape[0] == "parallelepiped" and parallelepiped.volume(shape) >= volume_value or \
                shape[0] == "tetrahedron" and tetrahedron.volume(shape) >= volume_value:
            new_container.append(shape)
    new_container
    return new_container
