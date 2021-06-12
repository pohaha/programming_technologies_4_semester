import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
import LAB7_VAR6
import numpy as np
plotting_tests = TESTING_MODULE.Test(LAB7_VAR6.plot_CTFs,
                                     "Тесты отрисовки графиков плотности распределения для случайных величин распределенных согласно нормальному(Гауссовому) закону распределения")
plotting_tests.add_case(
    "Количество аргументов - без аргументов", LAB7_VAR6.ERROR_MESSAGES[0])
plotting_tests.add_case(
    "Тип аргументов - для введенного напрямую набора данных - тип данных не число", LAB7_VAR6.ERROR_MESSAGES[1], 1, 2)
plotting_tests.add_case(
    "Тип аргументов - один аргумент не являющийся контейнером", LAB7_VAR6.ERROR_MESSAGES[1], 10)
plotting_tests.add_case(
    "Тип аргументов - в одном наборе данных - не верное количество аргументов", LAB7_VAR6.ERROR_MESSAGES[1], [1, 2, 3])
plotting_tests.add_case(
    "Тип аргументов - в одном наборе данных - аргумент не является числом", LAB7_VAR6.ERROR_MESSAGES[1], [1, "П"])
plotting_tests.add_case(
    "Тип аргументов - несколько аргументов не интерпретируемых как наборы данных для построения графиков плотности распределения", LAB7_VAR6.ERROR_MESSAGES[1], 10, 9)
plotting_tests.add_case(
    "Тип аргументов - для нескольких введенных наборов данных - не верное количество аргументов", LAB7_VAR6.ERROR_MESSAGES[1], [1, 2], (2, 3, 4))
plotting_tests.add_case(
    "Тип аргументов - для нескольких введенных наборов данных - аргумент не является числом", LAB7_VAR6.ERROR_MESSAGES[1], [1, 2], ["G", 10])
plotting_tests.add_case(
    "Правильно введенные данные - один набор", 0, [0, 1])

plotting_tests.run()
