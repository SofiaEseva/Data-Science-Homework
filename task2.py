import time
a = int(input('Введите время в секундах: '))
time_format = time.strftime('%H:%M:%S', time.gmtime(a))
print('Количество введеных секунд составляет ',time_format)

