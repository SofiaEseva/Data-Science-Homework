#Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('Машина повернула')
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print (self.speed)

class SportCar(Car):

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        else:
            print(self.speed)

class PoliceCar(Car):

a = TownCar (55, 'blue', 'Max', False)
b = SportCar (120, 'red', 'Adriano', False)
c = WorkCar (45, 'yellow', 'Steeven', False)
d = PoliceCar (80, 'white', 'Ron', True)
print(a.show_speed())
# Выдает ошибку, хотя здесь не нужен отступ
#class WorkCar(Car):
#    ^
#IndentationError: expected an indented block