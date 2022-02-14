#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
my_file = open('my_file.txt', 'w')
while True:
    new_str = input('Введите строку: ')
    if new_str == '':
        break
    my_file.write(new_str + '\n')
my_file.close()
my_file = open('my_file.txt')
content = my_file.read()
print(content)






