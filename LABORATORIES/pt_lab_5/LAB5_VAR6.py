import numbers
ERROR_MESSAGES = ["argument count error", "argument type error"]


def sign_changes(*args):
    if(len(args) == 0):
        print("проверьте число аргументов в функции - нет аргументов")
        return ERROR_MESSAGES[0]
    elements = args
    output_message = str()
    if(len(args) == 1):
        if(isinstance(args[0], numbers.Number)):
            output_message = "в функцию подано всего 1 число"
            print(output_message)
            return 0
        try:
            elements = iter(args[0])
        except TypeError:
            output_message = "всего в функцию подан один аргумент и он не является итеррируемым контейнером"
            print(output_message)
            return ERROR_MESSAGES[1]
        if(len(args[0]) == 1):
            output_message = "в поданном в функцию контейнере всего один элемент"
            print(output_message)
            return 0
    error_state = False
    first_element = True
    rt_val = 0
    current_sign = 0
    next_sign = 0
    for el in elements:
        if(error_state == False):
            output_message = "что-то не так с хотябы одним элементом:"
        if(not isinstance(el, numbers.Number)):
            error_state = True
            output_message += (F"\n\tэлемент {el} не является числом")
        else:
            if(first_element):
                current_sign = next_sign = (el > 0)
                first_element = False
            next_sign = (el > 0)
            if(next_sign != current_sign):
                rt_val += 1
            current_sign = next_sign
        if(el == 0):
            error_state = True
            output_message += (F"\n\tэлемент {el} = 0")
    if (error_state == True):
        print(output_message)
        return ERROR_MESSAGES[1]
    output_message = F"в поданной последовательности чисел наблюдается всего {rt_val} изменений знаков"
    print(output_message)
    return rt_val
