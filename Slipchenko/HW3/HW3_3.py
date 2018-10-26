input_user = int(input('Enter number: '))

list_numbers = list(range(2, input_user + 1))
print(list_numbers)

for number in list_numbers:
    if number != 0:
        for element in range(2 * number, input_user+1, number):
            list_numbers[element-2] = 0

list_new = [i for i in list_numbers if i != 0]
print(list_new)
