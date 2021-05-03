"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import randint

massiv = [randint(-100, -1) for i in range(randint(5, 15))]
print(f"Исходный массив: {massiv}")
min_num = min(massiv)
min_num_count = massiv.count(min_num)
massiv = list(filter(lambda x: x != min_num, massiv))
min_num_s = min(massiv)
print(
    f"Наименьший элемент: {min_num}, встречается в этом массиве {min_num_count} раз\n"
    f"Второй наименьший элемент: {min_num_s}"
)
