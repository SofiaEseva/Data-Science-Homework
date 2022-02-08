def my_div ():
    """Выполняет деление двух запрашиваемых чисел"""
    arg_1 = float(input('Введите первое число: '))
    arg_2 = float(input('Введите второе число: '))
    return arg_1/arg_2
try:
    print(my_div())
except BaseException:
    print('На ноль делить нельзя!')
