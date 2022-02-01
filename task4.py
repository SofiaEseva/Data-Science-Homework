a = abs(int(input('Введите целое положительное число: ')))
max = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max:
        max = a % 10
    if a > 9:
        continue
    else:
        print('Наибольшая цифра в числе ', max)
    break