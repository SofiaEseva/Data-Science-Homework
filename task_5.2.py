#Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
f = open('my_file_2.txt')
print('Количество строк в файле: ', len(f.readlines()))
f.close()

f = open('my_file_2.txt')
i = 0
content = f.readlines()
while i < len(content):
    print('Количество слов в строке №', i+1, '=', len(content[i].split(' ')))
    i+=1
f.close()