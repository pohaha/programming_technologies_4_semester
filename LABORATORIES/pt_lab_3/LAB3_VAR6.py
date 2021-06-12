

import numbers
ERROR_MESSAGES = ["argument count error", "argument type error"]


def row_summ(*args):
    if(len(args) != 1):
        print("проверьте правильность введенный данных - неверное количество аргументов!")
        return ERROR_MESSAGES[0]
    if(not isinstance(args[0], numbers.Number)):
        print("проверьте правильность введенный данных - аргумент не является числом")
        return ERROR_MESSAGES[1]
    row_counter = args[0]
    if((row_counter % 1) != 0):
        print("проверьте правильность введенных аргументов - аргумент не является целым числом")
        return ERROR_MESSAGES[1]
    rt_value = 0
    for n in range(row_counter):
        rt_value += (2*n+1)
    print(F"результат выполнения функции - {rt_value}")
    return rt_value
