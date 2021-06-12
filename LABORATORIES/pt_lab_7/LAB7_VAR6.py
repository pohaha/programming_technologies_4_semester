import numbers
import numpy as np
import matplotlib.pyplot as plt
ERROR_MESSAGES = ["argument count error", "argument type error"]
N = 10000


def plot_CTFs(*args):
    if(len(args) == 0):
        print("Введено недостаточно аргументов")
        return ERROR_MESSAGES[0]
    data_set_number = 0
    error_state = False
    error_msg = "В интерпретации введенных наборов встретились ошибки:\n"
    x_sets = []
    for data_set_items in args:
        data_set_number = data_set_number+1
        try:
            iter(data_set_items)
        except:
            error_state = True
            error_msg = error_msg + \
                F"\tНабор #{data_set_number} нельзя интерпретировать как набор данных формата [μ,σ²] так как он не является контейнером\n"
        else:
            if(len(data_set_items) != 2):
                error_state = True
                error_msg = error_msg + \
                    F"\tНабор #{data_set_number} нельзя интерпретировать как набор данных формата [μ,σ²] так как его длина = {len(data_set_items)}\n"
                continue
            data_set = {
                "μ": data_set_items[0],
                "σ²": data_set_items[1]
            }
            for item in data_set:
                if(not isinstance(data_set[item], numbers.Number)):
                    error_state = True
                    error_msg = error_msg + \
                        F"\tВ наборе #{data_set_number} элемент {item} не является числом, но элементом  типа {type(data_set[item])}\n"
            if(not error_state):
                data = np.random.normal(
                    loc=data_set["μ"], scale=data_set["σ²"]**0.5, size=N)
                x_sets.append(np.sort(data))
    y_set = (np.arange(N)/float(N))
    if(error_state == True):
        print(error_msg)
        return ERROR_MESSAGES[1]
    for i in range(len(x_sets)):
        plt.plot(x_sets[i], y_set,)
    plt.show()
    return 0
