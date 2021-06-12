import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8
import TESTING_MODULE

determinant_tests = TESTING_MODULE.Test(
    LAB6_VAR6.determinant, "поиск определителя матрицы разложением по строке")
determinant_tests.add_case(
    "количество аргументов - без аргументов", LAB6_VAR6.ERROR_MESSAGES[0])
determinant_tests.add_case(
    "количество аргументов - много аргументов", LAB6_VAR6.ERROR_MESSAGES[0], [[1, 2], [1, 2]], 10)
determinant_tests.add_case(
    "тип аргументов - не коллекция", LAB6_VAR6.ERROR_MESSAGES[1], 10)
determinant_tests.add_case(
    "тип аргументов - коллекция состоящая не из коллекций", LAB6_VAR6.ERROR_MESSAGES[1], [123, 321])
determinant_tests.add_case(
    "тип аргументов - коллекция состоящая из коллекций разной длинны", LAB6_VAR6.ERROR_MESSAGES[1], [(1, 2, 3), [3, 2]])
determinant_tests.add_case(
    "тип аргументов - внутренние коллекции состоят не из чисел", LAB6_VAR6.ERROR_MESSAGES[1], [(1, 2, 3), "Паша"])
determinant_tests.add_case(
    "Математика - поданная матрица не является квадратной", LAB6_VAR6.ERROR_MESSAGES[2], [(1, 2, 3), (3, 2, 1)])
determinant_tests.add_case(
    "Правильно введенные данные - простой случай (матрица 2х2)", -4, [(1, 2), (3, 2)])
determinant_tests.add_case(
    "Правильно введенные данные - сложный случай (матрица 3х3 и далее)", 0, [(1, 2, 3), (4, 5, 6), (7, 8, 9)])


determinant_tests.run()
