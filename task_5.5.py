with open('my_file_5.txt', 'w') as my_file:
    my_file = my_file.write('23 45 56 123 17 68 13')
with open ('my_file_5.txt') as my_file:
    my_list = list(my_file.readline().split(' '))
    my_list_2 = [float(i) for i in my_list]
    print(sum(my_list_2))

