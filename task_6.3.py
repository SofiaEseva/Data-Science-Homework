class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        my_dict = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = my_dict
class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Анатолий', 'Печкин', 'Врач', 20000, 15000)
b = Position('Евгений', 'Человечкин', 'Грач', 10000, 1500)
c = Position('Сергей', 'Стычкин', 'Богач', 80000, 45000)

print(a.get_full_name(), a.get_total_income())
print(b.get_full_name(), b.get_total_income())
print(c.get_full_name(), c.get_total_income())