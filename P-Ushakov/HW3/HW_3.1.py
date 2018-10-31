"""
Задача 3.1:
Написать алгоритм пузырьковой сортировки.
Вы должны создать список из случайных чисел и случайной длинны. Вывести его. Отсортировать НАПИСАННЫМ ВАМИ алгоритмом
пузырьковой сортировки и вывести отсортированный список. Отсортированные значение складывайте в отдельный список.
Естественно использовать sort и sorted нельзя
Пузырьковая сортировка - https://ru.wikipedia.org/wiki/Сортировка_пузырьком
"""
import random

input_list = []
sorted_list = []
# create random list with random float numbers
for x in range(1, random.randint(10, 300)):
    input_list.append(random.randint(1, 100000) / 100)
print(input_list)

# do sorting
sorted_list = input_list[:]
iterator = range(len(input_list) - 1)
while any(sorted_list[i] > sorted_list[i + 1] for i in iterator):
    for x in iterator:
        (w1, w2) = sorted_list[x:x+2]
        if w1 > w2:
            sorted_list[x:x+2] = (w2, w1)

print(sorted_list)
