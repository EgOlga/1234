import numpy as np
import pandas as pd

"""
Библиотека numpy предназначена для решения математических задач.
np.eye создаёт единичную матрицу
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
"""
print('numpy')
a = np.eye(7,7, dtype="int8")
print(a)
print()

b = np.array([1, 3, 5, 7, 9])
print(b)
print(b+1)
print(b*4)
print(b.dtype)
print()

"""
Библиотека рandas применяется для обработки и анализа табличных данных.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
"""
print('pandas')
table = pd.read_csv('pandas.txt', delimiter=';')
print(table)
print(table.head(3))
print(table.tail(3))
print()


