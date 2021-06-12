import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
import LAB4_VAR6

different_letters_tests = TESTING_MODULE.Test(
    LAB4_VAR6.different_letters, "Вычисление количества различных букв в тексте")

different_letters_tests.add_case(
    "количество аргументов - без аргументов", LAB4_VAR6.ERROR_MESSAGES[0])
different_letters_tests.add_case(
    "количество аргументов - много аргументов", LAB4_VAR6.ERROR_MESSAGES[0], "паша", "саша")
different_letters_tests.add_case(
    "тип аргументов - число", LAB4_VAR6.ERROR_MESSAGES[1], 6)
different_letters_tests.add_case(
    "тип аргументов - массив текстов", LAB4_VAR6.ERROR_MESSAGES[1], ["паша", "саша"])

different_letters_tests.add_case(
    "реальные данные - только разные буквы", 3, "123ert123")
different_letters_tests.add_case(
    "реальные данные - повторяющиеся буквы", 10, "Паша лучше всех")
different_letters_tests.add_case(
    "реальные данные - повторяющиеся буквы разных регистров", 10, "Паша лучше всех папаш")
different_letters_tests.run()
