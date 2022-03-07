class Clothes:
    def __init__(self, size, heigth):
        self.size = size
        self.height = heigth
class Coat(Clothes):
    def func_1(self):
        super().__init__(size, heigth)
        return f'Расход ткани {self.size / 6,5 + 0,5}'
class Costume(Clothes):
    def func_2(self):
        return f'Расход ткани {self.height * 2 + 0,3}'
mc = Clothes(42, 170)
print(mc(Coat(Clothes)))
