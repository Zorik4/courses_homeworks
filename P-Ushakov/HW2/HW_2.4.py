"""
Задача 2.4:
Тоже самое, только пирамидку:
Ввод: 3
Вывод:
  *
 * *
* * *
"""
# 2.4 Вторая пирамида
brick = ""
n_steps = input("Введите целое число до 20 для ступеней")
if not n_steps.isdigit():
    n_steps = 0
else:
    n_steps = int(n_steps) + 1

for i in range(1, n_steps):
    print(" " * (n_steps - i), " *" * i)