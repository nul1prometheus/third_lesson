# -*- coding: utf-8 -*-
import random
from random import random, randint, choice

import simple_draw as sd

sd.resolution = (1900, 1000)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 100)
radius = 50
for _ in range(3):
    radius += 5
    # sd.circle(center_position=point, radius=radius, width=2)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 25
    for _ in range(3):
        radius += 5
        sd.circle(center_position=point, radius=radius, color=[],width=2)

point = sd.get_point(300, 300)
# bubble(point = point, step=10)

# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 200)
#     bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 1101, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=1)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
a=1

while a== True:
    x=randint(1, 1900)
    y=randint(1, 1000)
    radius=randint(5, 100)
    width=randint(2, 7)
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, color=[r, g, b], width=width)
    sd.clear_screen()

sd.pause()


