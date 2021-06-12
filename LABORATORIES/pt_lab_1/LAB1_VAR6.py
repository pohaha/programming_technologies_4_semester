import numbers
import math

imported = True
ERROR_MESSAGES = ("argument count error", "argument type error!",
                  "zero division error!", "sqare root from negative number error!")


def run(*args):
    if(len(args) != 3):
        return ERROR_MESSAGES[0]
    is_number = True
    for arg in args:
        is_number = is_number and isinstance(arg, numbers.Number)
    if (not is_number):
        return ERROR_MESSAGES[1]
    a = args[0]
    """ if(a == 0):
        return ERROR_MESSAGES[2] """
    b = args[1]
    c = args[2]
    if(b**2-(4*a*c) < 0):
        return ERROR_MESSAGES[3]
    x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    value = (math.exp(x_1)+math.exp(x_2))/2
    return round(value, 4)
