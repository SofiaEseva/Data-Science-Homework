my_list = [1, 2, 2.5, True, 'word', 'number']
el1 = 'world'
el2 = 5
new_list = [-3, 'water', 'orange']
my_list.append(el1)
my_list.insert(5, el2)
my_list.extend(new_list)
my_list.remove('number')
my_list.pop(2)
print(my_list)
for el in range(len(my_list)):
     print(type(my_list[el]))
