#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month=int(input('Введите месяц в виде целого числа от 1 до 12 '))
my_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 1 or month == 2 or month == 12:
    print(my_list[0])
elif month == 3 or month == 4 or month == 5:
    print(my_list[1])
elif month == 6 or month == 7 or month == 8:
    print(my_list[2])
elif month == 9 or month == 10 or month == 11:
    print(my_list[3])
else: print('Ошибка')

key=int(input('Введите месяц в виде целого числа от 1 до 12 '))
my_dict = {
    (1, 2, 12) : 'Зима',
    3 : 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень'
}
print(my_dict[key])
#не получается сделать кортеж внутри, выдает ошибку. Не понимаю, как ее решить