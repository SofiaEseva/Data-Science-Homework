#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
with open('my_file_3.txt', 'r') as my_file:
    workers = {}
    for line in my_file:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(key)
    from statistics import mean
    my_list = list(workers.values())
    my_list_2 = [float(i) for i in my_list]
    aver = mean(my_list_2)
    print('Средняя зарплата', aver)