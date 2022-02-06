my_list = input("Введите элементы списка через пробел: ").split()
print(my_list)
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)
#вообще не поняла как это сделать - пришлось списать(