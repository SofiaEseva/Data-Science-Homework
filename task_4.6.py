from itertools import count, cycle
for el in count (3):
    if el > 10:
        break
    else:
        print(el)

c = 0
for el in cycle ('pararam'):
    if c > 20:
        break
    else:
        print(el)
        c +=1