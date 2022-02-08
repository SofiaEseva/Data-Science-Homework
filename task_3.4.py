def my_func ():
    """Возводит число в степень"""
    x = abs(float(input('Введите первое число: ')))
    y = int(input('Введите второе число: '))
    return x**y
print(my_func())

def my_func ():
    """Возводит число в отрицательную степень"""
    x = abs(float(input('Введите первое число: ')))
    y = int(input('Введите второе число: '))
    i = 1
    result = x
    while i < abs(y):
        result *= x
        i += 1
    return 1 / result
print(my_func())