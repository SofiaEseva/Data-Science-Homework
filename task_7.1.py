class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1
    def __str__(self):
        return str(self.list_1)
mc = Matrix ([[31, 32], [33, 34], [35, 36]])
print(mc)

from itertools import chain
class Matrix:
    def __init__(self, list_1):
        self.list_1 = list(chain(*list_1))
    def __add__(self, other):
        for i in range(len(self.list_1)):
            return Matrix(self.list_1[i] + other.list_1[i])
    def __str__(self):
        return f'Сумма матриц {self.list_1}'
mc_1 = Matrix ([[31, 32], [33, 34], [35, 36]])
mc_2 = Matrix ([[1, 2], [3, 4], [5, 6]])
print(mc_1 + mc_2)
