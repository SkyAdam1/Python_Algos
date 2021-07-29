"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random


def list_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    left_part, right_part = list_sort(array[:middle]), list_sort(array[middle:])
    return list_merge(left_part, right_part)


def list_merge(list_1, list_2):
    result = []
    i, j = 0, 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    return result + list_1[i:] + list_2[j:]


LIST_SIZE = int(input("Введите число элементов: "))
NUMS = [random() * 50 for i in range(LIST_SIZE)]

print(NUMS)
print(list_sort(NUMS))
