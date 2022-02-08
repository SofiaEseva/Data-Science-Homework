def int_func():
    """Принимает слова из маленьких букв возвращает их же но с заглавной """
    text = input('Введите слова: ').lower()
    return text.title()
print(int_func())