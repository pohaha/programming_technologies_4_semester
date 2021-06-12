import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
import LAB8_VAR6
parse_table_tests = TESTING_MODULE.Test(
    LAB8_VAR6.parse_table, "Обработка таблицы CSV")
parse_table_tests.add_case(
    "Количество аргументов - без аргументов", LAB8_VAR6.ERROR_MESSAGES[0])
parse_table_tests.add_case(
    "Тип аргументов - аргумент не являющийся текстовой строкой", LAB8_VAR6.ERROR_MESSAGES[1], 10)
parse_table_tests.add_case(
    "Тип аргументов - аргумент не являющийся путем к файлу", LAB8_VAR6.ERROR_MESSAGES[1], "gfif")
parse_table_tests.add_case(
    "Тип аргументов - аргумент не являющийся путем к файлу CSV", LAB8_VAR6.ERROR_MESSAGES[1], "showcase.py")
test_data = [{"name": "Pavel",
              "occupation": "Programmer"}]
parse_table_tests.add_case(
    "правильно введенные данные - файл с одной строкой", test_data, "test_csv.csv")
# parse_table_tests.run()

draw_dependance_graphs_tests = TESTING_MODULE.Test(
    LAB8_VAR6.draw_dependancy_graphs, "Отрисовка графиков зависимости")
draw_dependance_graphs_tests.add_case(
    "Количество аргументов - без аргументов", LAB8_VAR6.ERROR_MESSAGES[0])
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - один аргумент не являющийся строкой, или контейнером", LAB8_VAR6.ERROR_MESSAGES[1], 10)
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - один аргумент являющийся строкой - название страны не встречается в файле", LAB8_VAR6.ERROR_MESSAGES[2], "АУЕ")
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - один аргумент являющийся контейнером - в котором встречается аргумент не являющийся строкой", LAB8_VAR6.ERROR_MESSAGES[1], ["AUS", 1])
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - один аргумент являющийся контейнером - одна из строк в котором не встречается как название страны в исходном файле", LAB8_VAR6.ERROR_MESSAGES[2], ["AUS", "hey"])
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - много аргументов, один или несколько из которых не являются строками", LAB8_VAR6.ERROR_MESSAGES[1], "hello", "i'm", 10, "mad")
draw_dependance_graphs_tests.add_case(
    "Тип аргументов - много аргументов, являющихся строками, одна из которых не встречается как название страны в исходном файле", LAB8_VAR6.ERROR_MESSAGES[2], "hello", "AUS", "USA", "RUS")
# draw_dependance_graphs_tests.run()

task_3_tests = TESTING_MODULE.Test(LAB8_VAR6.task_3, "Задание 3 - вариант 'C'")
task_3_tests.add_case(
    "Количество аргументов - неверное число аргументов", LAB8_VAR6.ERROR_MESSAGES[0])
task_3_tests.add_case(
    "Тип аргументов - один из введенных параметров - не число", LAB8_VAR6.ERROR_MESSAGES[1], 10, "G")
task_3_tests.add_case(
    "Тип аргументов - один из введенных параметров - не целое число", LAB8_VAR6.ERROR_MESSAGES[1], 10, 10.5)
task_3_tests.add_case(
    "Правильно введенные данные", LAB8_VAR6.ERROR_MESSAGES[1], 2, 2)

task_3_tests.run()
