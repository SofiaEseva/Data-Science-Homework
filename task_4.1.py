def salary():
    try:
        hour = float(input('Количество отработанных часов: '))
        payment = float(input('Почасовая ставка: '))
        money = float(input('Сумма премии за месяц: '))
        return (hour * payment) + money
    except ValueError:
        return print('Введены некорректные значения')
print(f'Заработная плата сотрудника {salary()} руб')
