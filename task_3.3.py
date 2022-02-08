def my_func ():
    """Возвращает сумму двух наибольших аргументов"""
    arg_1 = float(input('Введите первое число: '))
    arg_2 = float(input('Введите второе число: '))
    arg_3 = float(input('Введите третье число: '))
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(my_list))
    return sum(my_list)
print(f'Сумма наибольших аргументов = {my_func()}')