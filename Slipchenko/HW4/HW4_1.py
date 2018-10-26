attempt = 0

while attempt < 3:
    user_input = input('Enter year: ')
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input % 4 == 0:
            print('{} is leap year'.format(user_input))
            exit()
        elif user_input % 4 >= 2:
            print('{} closest high year'.format(int(4 * (user_input // 4))+4))
            exit()
        else:
            print('{} closest high year'.format(int(4 * (user_input // 4))))
            exit()
    else:
        print('Is not year')
        attempt += 1
print('Most likely your hands grow out of ass or you are blind')
