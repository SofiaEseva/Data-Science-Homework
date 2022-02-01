a = int(input("Введите расстояние в первый день бега "))
b = int(input("Введите целевое расстояние "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print('Вы достигнете желаемого расстояния бега на', result_days, 'день')