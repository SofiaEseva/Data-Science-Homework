from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running():
        i = 0
        while i < 20: #это я типа зациклила
            print('Цвет светофора ', TrafficLight.__color[i % 3])
            if i % 3 == 0:
                sleep(7)
            elif i % 3 == 1:
                sleep(2)
            elif i % 3 == 2:
                sleep (5)
            i += 1
print(TrafficLight.running())