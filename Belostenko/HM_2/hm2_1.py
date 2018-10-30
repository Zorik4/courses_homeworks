import random
from string import ascii_letters as letters, digits as digit
list_string = []
list_num = []
dictionary = {}
for i in range(10):
    length = random.randint(1, 10)
    element = random.sample(letters, length)
    element = "".join(element)
    list_string.append(element)
    length = random.randint(1, 10)
    number = random.sample(digit, length)
    number = "".join(number)
    list_num.append(number)
    dictionary.update({list_string[i]: list_num[i]})
print("Strings = ",list_string)
print("Numbers = ", list_num)
print("Dictionary = ", dictionary)
