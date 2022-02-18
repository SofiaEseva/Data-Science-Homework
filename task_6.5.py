#Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#оздать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw():
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Рисует', self.title)
class Pencil(Stationery):
    def draw(self):
        print('Рисует', self.title)
class Handle(Stationery):
    def draw(self):
        print('Рисует', self.title)
a = Pen('ручка')
b = Pencil('карандаш')
c = Handle('маркер')

print(a.draw())
print(b.draw())
print(c.draw())