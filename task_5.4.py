#Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
#числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('my_file_4.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(my_dict[i[0]] + '  ' + i[1])
    print(new_file)

with open('My_file_4.1.txt', 'w') as my_file_2:
    my_file_2.writelines(new_file)