﻿name = input("Как Вас зовут? ")
print ('Привет, ', name, '! Сейчас мы выполним простые операции на числах')
a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))
print('Сумма введенных чисел равна ', a + b, '\nРазница введенных чисел равна ', a - b,
      '\nПроизведение введенных чисел равно ', a * b, '\nДеление введенных чисел равно ', format ( a / b, '.1f'))