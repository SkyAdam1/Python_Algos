"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import randint

a = randint(0 , 100)
attempts = 10
while True:
    if attempts == 0:
        print(f"Вы не угадали, это было число {a}")
        break
    b = int(input("Угадайте число: "))
    if a == b:
        print(f"Вы угадали, это было число {b}")
        break
    elif a > b:
        attempts -= 1
        print(f"Загаданное число больше, чем {b}")
    elif a < b:
        attempts -= 1
        print(f"Загаданное число меньше, чем {b}")
    