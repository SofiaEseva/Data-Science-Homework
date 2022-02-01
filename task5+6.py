revenue = float(input('Введите выручку фирмы в рублях '))
costs = float(input('Введите издержки фирмы в рублях '))
if revenue > costs:
    print('Фирма работает в плюс. Рентабельность выручки составила ', format(revenue / costs, '.2f'))
    workers = int(input('Введите количество сотрудников фирмы '))
    print('Прибыль в расчете на одного сторудника сотавила', format(revenue / workers,'.2f'), ' рублей')
elif revenue == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток. Убыток составил ', format(revenue - costs,'.2f'), ' рублей')