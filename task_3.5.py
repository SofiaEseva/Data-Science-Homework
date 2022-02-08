def my_func():
    """Выводится сумма чисел написанных через пробел"""
    numbers = input('Введите числа через пробел: ')
    my_list = numbers.split(' ')
    for i in range(len(my_list)):
         my_list[i] = int(my_list[i])
    return sum(my_list)
print(my_func())
#Не поняла, как сделать, чтобы пользователь продолжал вводить числа, а списывать не хотелось