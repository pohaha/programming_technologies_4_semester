import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE
from random import randint
import LAB1_VAR6

TEST_LAB1_VAR6 = TESTING_MODULE.Test(LAB1_VAR6.run)

TEST_LAB1_VAR6.add_case(
    "0 arguments", LAB1_VAR6.ERROR_MESSAGES[0])

TEST_LAB1_VAR6.add_case(
    "4 arguments", LAB1_VAR6.ERROR_MESSAGES[0], randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

TEST_LAB1_VAR6.add_case(
    "argument type", LAB1_VAR6.ERROR_MESSAGES[1], 1, "Pavel", randint(0, 10))

TEST_LAB1_VAR6.add_case(
    "zero division", LAB1_VAR6.ERROR_MESSAGES[2], 0, randint(0, 10), randint(0, 10))

TEST_LAB1_VAR6.add_case(
    "sqare root from negative number", LAB1_VAR6.ERROR_MESSAGES[3], 2, 3, 2)

TEST_LAB1_VAR6.add_case(
    "arithmetic 1'st", 0.2516, 1, 3, 2)

TEST_LAB1_VAR6.add_case(
    "arithmetic 2'nd", 0.2955, 2, 5, 3)

TEST_LAB1_VAR6.run()
