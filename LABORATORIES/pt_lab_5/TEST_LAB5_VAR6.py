import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
import LAB5_VAR6

sign_change_tests = TESTING_MODULE.Test(
    LAB5_VAR6.sign_changes, "расчет изменения знаков")
sign_change_tests.add_case(
    "количество аргументов - без аргументов", LAB5_VAR6.ERROR_MESSAGES[0])
sign_change_tests.add_case(
    "тип аргументов - один аргумент не вляющийся итеррируемым, или числовым", LAB5_VAR6.ERROR_MESSAGES[1], object())
sign_change_tests.add_case(
    "тип аргументов - много элементов хотябы один из которых не является числовым", LAB5_VAR6.ERROR_MESSAGES[1], "Pavel", 1, -2, 3, -4)
sign_change_tests.add_case(
    "тип аргументов - один элемент являющийся контейнером в котором хотябы один элемент не является числом", LAB5_VAR6.ERROR_MESSAGES[1], ["Pavel", 1, -2, 3, -4])
sign_change_tests.add_case(
    "тип аргументов - хотябы один из числовых элементов равен 0", LAB5_VAR6.ERROR_MESSAGES[1], [1, -2, 0, -4])
sign_change_tests.add_case(
    "тип аргументов - всего одно число в контейнере с числами", 0, [1])
sign_change_tests.add_case(
    "тип аргументов - всего одно число", 0, 1)
sign_change_tests.add_case(
    "правильно введенные аргументы - два числа с не меняющимся знаком", 0, 1, 2)
sign_change_tests.add_case(
    "правильно введенные аргументы - два числа с меняющимся знаком", 1, 1, -2)
sign_change_tests.add_case(
    "правильно введенные аргументы - несколько чисел с меняющимся знаком", 3, 1, -2, 1, 1, 1, -32)
sign_change_tests.add_case(
    "правильно введенные аргументы - контейнер с несколькими числами с меняющимся знаком", 3, [1, -2, 1, 1, 1, -32])


sign_change_tests.run()
