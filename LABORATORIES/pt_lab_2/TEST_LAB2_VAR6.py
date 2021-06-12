import sys  # nopep8
sys.path.append('../../TESTING_MODULE')  # nopep8

import TESTING_MODULE

import LAB2_VAR6


quadratic_function_extraction_test = TESTING_MODULE.Test(
    LAB2_VAR6.quadratic_function_from_focus_and_horizontal_line_extraction, "extracting quadratic function from point and line")
quadratic_function_extraction_test.add_case(
    "argument count", LAB2_VAR6.ERROR_MESSAGES[0])
quadratic_function_extraction_test.add_case(
    "argument type - not a 2d point 1", LAB2_VAR6.ERROR_MESSAGES[1], ("pasha", 3), "pasha")
quadratic_function_extraction_test.add_case(
    "argument type - not a 2d point 2", LAB2_VAR6.ERROR_MESSAGES[1], 3, "pasha")
quadratic_function_extraction_test.add_case(
    "argument type - not a 2d point 3", LAB2_VAR6.ERROR_MESSAGES[1], (3, 3, 3), "pasha")
quadratic_function_extraction_test.add_case(
    "argument type - not a horizontal line", LAB2_VAR6.ERROR_MESSAGES[1], (3, 3), "pasha")
quadratic_function_extraction_test.add_case(
    "math - focus is placed on the directrix", LAB2_VAR6.ERROR_MESSAGES[2], (3, 3), 3)
quadratic_function_extraction_test.add_case(
    "math - successfull quadratic function extraction", {"a": 0.1, "b": -0.4, "c": 2.9}, {2, 5}, 0)
quadratic_function_extraction_test.run()

finding_intersection_lines_function_tests = TESTING_MODULE.Test(
    LAB2_VAR6.find_quadratic_functions_intersections, "finding intersections between 2 quadratic functions")
finding_intersection_lines_function_tests.add_case(
    "argument count - no arguments", LAB2_VAR6.ERROR_MESSAGES[0])
finding_intersection_lines_function_tests.add_case(
    "argument count - too many arguments", LAB2_VAR6.ERROR_MESSAGES[0], 2, 2, 2)
finding_intersection_lines_function_tests.add_case(
    "argument type - not a dictionary", LAB2_VAR6.ERROR_MESSAGES[1], 2, 2)
finding_intersection_lines_function_tests.add_case(
    "argument type - not convertable to a quadratic function", LAB2_VAR6.ERROR_MESSAGES[1], {"a": 0}, {"a": 0})
finding_intersection_lines_function_tests.add_case(
    "math - no intersections between quadratic functions - 1", LAB2_VAR6.ERROR_MESSAGES[2], {"a": 10, "b": 15, "c": 5}, {"a": 2, "b": 11, "c": 3})
finding_intersection_lines_function_tests.add_case(
    "math - two identical quadratic functions", LAB2_VAR6.ERROR_MESSAGES[2], {"a": 10, "b": 15, "c": 5}, {"a": 10, "b": 15, "c": 5})
finding_intersection_lines_function_tests.add_case(
    "math - a1=a2; b1=b2", LAB2_VAR6.ERROR_MESSAGES[2], {"a": 10, "b": 15, "c": 5}, {"a": 10, "b": 15, "c": 3})
finding_intersection_lines_function_tests.add_case(
    "math - a1=a2", [(-0.4, round(0.6, 4))], {"a": 10, "b": 15, "c": 5}, {"a": 10, "b": 10, "c": 3})
finding_intersection_lines_function_tests.add_case(
    "math - example with 1 intersection", [(-1, 0)], {"a": 7, "b": 16, "c": 9}, {"a": 5, "b": 12, "c": 7})
finding_intersection_lines_function_tests.add_case(
    "math - example with 2 intersections", [(0, 7), (-1.5, -1.25)], {"a": 7, "b": 16, "c": 7}, {"a": 5, "b": 13, "c": 7})

finding_intersection_lines_function_tests.run()

task_function_tests = TESTING_MODULE.Test(
    LAB2_VAR6.task_function, "finding intersections between 2 parabolas cpecified by their focus and directrix parallel to abscis axis")
task_function_tests.add_case(
    "argument count - no arguments", LAB2_VAR6.ERROR_MESSAGES[0])
task_function_tests.add_case(
    "argument count - too many argumenst", LAB2_VAR6.ERROR_MESSAGES[0], 1, 2, 3, 4)
task_function_tests.add_case(
    "argument type - not a point", LAB2_VAR6.ERROR_MESSAGES[1], "pasha", 1, 2)
task_function_tests.add_case(
    "argument type - not a line", LAB2_VAR6.ERROR_MESSAGES[1], "pasha", (1, 2), (2, 3))
task_function_tests.add_case(
    "math - two identical points", LAB2_VAR6.ERROR_MESSAGES[2], 5, (2, 3), (2, 3))
task_function_tests.add_case(
    "math - example with 2 intersections", [(2.2111, 2.9445), (-12.2111, 75.0555)], 0, (0, 1), (5, 2))


task_function_tests.run()
