"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

count_num = int(input("Сколько будет чисел? "))
c = int(input("Какую цифру будем считать? "))
count = 0
for i in range(1, count_num + 1):
    m = int(input(f"Введите число {i} "))
    while m > 0:
        if m % 10 == c:
            count += 1
        m = m // 10

print(f"Было введено {count} цифр {c}")
