my_list = input('Введите числа через пробел: ').split(' ')
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
new_list = (el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num])
print(type(new_list))
print(list(new_list))