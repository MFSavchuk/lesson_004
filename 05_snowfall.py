# -*- coding: utf-8 -*-

import simple_draw as sd

sd.background_color = sd.COLOR_BLACK

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

N = 30  # количество снежинок
x_cords = []  # координаты x
y_cords = []  # координаты y
sizes = []  # размеры снежинок
snowflakes = []  # список снежинок
factor_a = []
factor_b = []
factor_c = []
count = 0  # счетчик для увеличения сугроба

while True:
    if count > 100:
        print('Высота сугроба 100мм')
        break
    for i in range(N):
        random = sd.random_number(0, 600)
        x_cords.append(random)

        random = sd.random_number(600, 1200)
        y_cords.append(random)

        random = sd.random_number(15, 50)
        sizes.append(random)

        random = float((sd.random_number(50, 70)) / 100)
        factor_a.append(random)

        random = float((sd.random_number(20, 40)) / 100)
        factor_b.append(random)

        random = sd.random_number(55, 65)
        factor_c.append(random)

    while True:
        sd.clear_screen()
        if max(y_cords) < 500:
            count += 20
            break

        for i in range(len(y_cords)):
            if y_cords[i] < sd.random_number(25+count, 49+count):
                center_point = sd.get_point(x_cords[i], y_cords[i])
                sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                             factor_b=factor_b[i], factor_c=factor_c[i])
                continue

            wind = sd.random_number(-5, 5)
            center_point = sd.get_point(x_cords[i] - wind, y_cords[i])
            sd.snowflake(center=center_point, length=sizes[i], color=sd.COLOR_WHITE, factor_a=factor_a[i],
                         factor_b=factor_b[i], factor_c=factor_c[i])
            y_cords[i] -= sd.random_number(2, 10)

        sd.sleep(0.1)
        if sd.user_want_exit():
            break
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
