def my_func ():
    """Выводит данные о пользователе одной строкой"""
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    e_mail = input('Введите е-майл: ')
    phone = input('Введите номер телефона: ')
    return ''.join(f' Имя - {name}, фамилия - {surname}, год рождения - {year}, город проживания - {city}, e-mail - {e_mail}, телефон - {phone}')
print(my_func())