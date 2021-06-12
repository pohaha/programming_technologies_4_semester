import numbers
ERROR_MESSAGES = ["argument count error", "argument type error", "math error"]


def determinant(*args):
    if(len(args) != 1):
        return ERROR_MESSAGES[0]
    try:
        lines = iter(args[0])
    except TypeError:
        print("введенный аргумент не является итеррируемым типом - невозможно преобразовать в матрицу")
        return ERROR_MESSAGES[1]
    height = len(args[0])
    array = []
    error_msg = "Возникли ошибки во время преобразования входных данных:\n"
    error_state = False
    first = True
    width = 0
    for line in lines:
        try:
            iter(line)
        except TypeError:
            error_msg = error_msg + \
                F"\tстрока #{len(array)+1} входной матрицы не является итеррируемой\n"
            error_state = True
        else:
            if(first):
                width = len(line)
                first = False
            if(len(line) != width):
                error_msg = error_msg + \
                    F"\tстрока #{len(array)+1} должна быть длинной {width} элементов, но была подана длинной {len(line)}\n"
                error_state = True
            for element in line:
                if(not isinstance(element, numbers.Number)):
                    error_msg = error_msg + \
                        F"\tстрока #{len(array)+1} элемент #{element} не является числом\n"
                    error_state = True
        finally:
            array.append(line)
    if(error_state == True):
        print(error_msg)
        return ERROR_MESSAGES[1]
    if(width != height):
        error_msg = F"Матрица не является квадратной:\n\tширина: {width}\n\tвысота: {height}\n"
        print(error_msg)
        return ERROR_MESSAGES[2]
    determinant_value = 0
    if(width == 2):
        determinant_value = array[0][0]*array[1][1]-array[0][1]*array[1][0]
        return determinant_value
    print(F"Now calculating complex matrix: {array}")
    for column in range(0, width):
        lesser_matrix = [[array[i][j] for j in range(
            0, width) if j != column] for i in range(1, height)]
        print(F"\tthe minor for column #{column} is:\n\t\t {lesser_matrix}")
        if((1+(column+1)) % 2 == 0):
            determinant_value = determinant_value + \
                array[0][column]*determinant(lesser_matrix)
            continue
        determinant_value = determinant_value - \
            array[0][column]*determinant(lesser_matrix)
    return determinant_value
