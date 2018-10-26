import random

list_random = random.sample(range(100), random.randint(2, 10))

print(list_random)

n = 0
len1 = len(list_random) - 1
while n < len1:
    if list_random[n] > list_random[n + 1]:
        list_random[n], list_random[n + 1] = \
            list_random[n + 1], list_random[n]
        n = 0
    else:
        n += 1

print(list_random)
