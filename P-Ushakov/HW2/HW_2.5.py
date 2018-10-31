"""
Задача 2.5:
Создайте список из случайных чисел,
отсортируйте его по убыванию, для каждого элемента списка создайте строку,
начинающуюся на букву, номер которой это это число
"""

import random
# создаю список из случайных чисел
li = []
for i in range(0, random.randint(5, 15)):
    li.append(random.randint(65, 91))
    li.append(random.randint(97, 122))
print(li)

# сортирую по убыванию
li.sort(reverse=True)
print(li)

# для каждого элемента списка создаю строку, начинающуюся на букву, номер которой это это число
str_li = []
for i in li:
    str_li.append(chr(i))
print(str_li)
