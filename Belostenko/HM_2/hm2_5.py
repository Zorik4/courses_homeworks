from random import randint
from string import ascii_uppercase as uppercase

rand_list = []
for i in range(randint(3, 10)):
    rand_list.append(randint(1, len(uppercase)))
print('Unsorted list: ', rand_list)
rand_list.sort(reverse = True)
sorted_list = rand_list
print('Sorted list: ', sorted_list)

letters_list = []
letters = []
for i in uppercase:
    letters.append(i)
for j in sorted_list:
    letters_list.append(letters[j-1])

letters_dict = dict(zip(sorted_list, letters_list))
print('Current numbers: ', letters_dict)
