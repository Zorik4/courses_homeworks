"""
Задача 3.3:
Взять число от пользователя и вывести все простые числа до это числа при помощи алгоритма решета Эратосфена
https://ru.wikipedia.org/wiki/Решето_Эратосфена
"""

try:
    input_int = int(input("Enter integer: "))
except ValueError:
    input_int = 0

list_of_numbers = [x for x in range(2, input_int + 1)]

start_point = 0
for number in list_of_numbers:
    start_point += 1
    cursor = start_point
    end_point = len(list_of_numbers)
    while cursor < end_point:
        if list_of_numbers[cursor] % number == 0:
            list_of_numbers.pop(cursor)
            end_point -= 1
        else:
            cursor += 1

print(list_of_numbers)

