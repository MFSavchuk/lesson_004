# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

x = [50, 100, 150, 200, 250, 300]


def generate(y_0):
    x1 = [50, 300]
    # sd.start_drawing()
    while True:
        for x2 in x1:
            point_0 = sd.get_point(x2, y_0)
            sd.snowflake(center=point_0, length=50, color=sd.background_color)
            sd.snowflake(center=point_0, length=50, color=sd.COLOR_WHITE)


        y_0 -= 10
        sd.snowflake(center=point_0, length=50, color=sd.background_color)
        sd.clear_screen()
        sd.sleep(0.1)
        if y_0 < 50:
            break
        generate(y_0)
        if sd.user_want_exit():
            break

generate(300)


# while True:
#     sd.clear_screen()
#     for x in x:
#         point = sd.get_point(x, y)
#         sd.snowflake(center=point, length=50)
#
#         sd.sleep(0.1)
#
#     if sd.user_want_exit():
#         break

# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#        break
#     x = x + 10
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 50:
#        break
#     x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
