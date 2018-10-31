"""
Задача 3.2
Написать маленькую программу, которая выведет саму себя при помощи файлов.
"""
import os
path = os.path.realpath(__file__)
with open(path, "r") as f:
    print("".join(f.readlines()))

