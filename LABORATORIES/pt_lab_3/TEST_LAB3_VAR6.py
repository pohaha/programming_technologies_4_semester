import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
import LAB3_VAR6

row_summ_test = TESTING_MODULE.Test(
    LAB3_VAR6.row_summ, "расчет суммы ряда по заданию")
row_summ_test.add_case("количество аргументов - без аргументов",
                       LAB3_VAR6.ERROR_MESSAGES[0])
row_summ_test.add_case("количество аргументов - много аргументов",
                       LAB3_VAR6.ERROR_MESSAGES[0], 10, 10)
row_summ_test.add_case("тип аргументов - не число",
                       LAB3_VAR6.ERROR_MESSAGES[1], "pavel")
row_summ_test.add_case("тип аргументов - не целое число",
                       LAB3_VAR6.ERROR_MESSAGES[1], 1.1)
row_summ_test.add_case("математика - рабочий набор аргументов",
                       25, 5)

row_summ_test.run()
