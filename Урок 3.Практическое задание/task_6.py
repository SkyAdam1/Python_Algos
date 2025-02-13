"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import randint

count = [
    randint(1, 100)
    for i in range(int(input("Введите количество элементов в массиве: ")))
]

maximum = count.index(max(count))
minimum = count.index(min(count))

summ = sum(
    i
    for i in range(
        minimum if maximum > minimum else maximum,
        maximum if maximum > minimum else minimum,
    )
)

print(f"Массив: {count}")
print(
    f"Сумма элементов между минимальным ({min(count)}) и максимальным ({max(count)}) элементами: {summ}"
)
