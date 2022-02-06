my_str = input("Напишите предложение ")
words = []
words = my_str.split()
num = 1
for el in range(my_str.count(' ') + 1):
    if len(str(words)) <= 10:
        print(num, words [el])
        num += 1
    else:
        print(num, words [el] [0:10])
        num += 1