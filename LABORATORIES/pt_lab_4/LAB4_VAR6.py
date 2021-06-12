ERROR_MESSAGES = ["argument count error", "argument type error"]


def different_letters(*args):
    if(len(args) != 1):
        print("ошибка - проверьте количество аргументов!")
        return ERROR_MESSAGES[0]
    text = args[0]
    if(type(text) != type(str())):
        print("введенный аргумент не является строкой")
        return ERROR_MESSAGES[1]
    if(not any([c.isalpha() for c in text])):
        print("во введенной строке нет ниодной буквы - это не текст")
        return ERROR_MESSAGES[1]
    fixed_text = str()
    letters_counter = 0
    for c in text:
        if c.isalpha():
            fixed_text += c
    fixed_text = fixed_text.lower()
    letters_counter = len(set(fixed_text))
    print(f"всего во введенном тексте {letters_counter} различных литер")
    return letters_counter
