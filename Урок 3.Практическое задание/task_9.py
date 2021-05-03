"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randint

row_count = int(input("Задайте количество строк в матрице: "))
column_count = int(input("Задайте количество столбцов в матрице: "))

matrix = list()
for i in range(column_count):
    matrix.append([randint(1, 100) for i in range(row_count)])
min_nums = [min(i) for i in matrix]
print(f"{min_nums} минимальные значения по столбцам")
print(f"Максимальное среди них = {max(min_nums)}")
