"""
Вам нужно реализовать шифратор и дешифратор шифра цезаря https://ru.wikipedia.org/wiki/Шифр_Цезаря
Примерный принцып работы такой:

Просите от пользователя ввод, для определения будет пользователь шифровать или дешифровать
2.1 Если шифровать - генерируете случайное число сдвига, выводите его и просите ввод от пользователя.
    Далее шифруете и записываете в файл. Выводите название файла и путь пользователю. завершаете программу
2.2 Если дешифровать - просите ввод сдвига, просите ввод пути к файлу, выводите дешифрованную инфу.
"""

import string

inp_key = input("Crypt - enter 'c', Decrypt - enter 'd': ")
# alphabet including symbols for coding
alphabet = list(string.ascii_letters + string.digits +
                'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзиклмнопрстуфхцчшщъыьэюя')
# we are decoding
if inp_key == "d":
    try:
        shift = int(input("Input shift to decode: "))
    except ValueError:
        print('Shift should be int')
        exit()

    # carousel ... # carousel
    cursor = 0
    decoder = alphabet[:]
    while cursor != shift:
        if shift < 0:
            decoder.insert(0, decoder.pop(len(decoder)-1))
            cursor -= 1
        elif shift > 0:
            decoder.append(decoder.pop(0))
            cursor += 1

    path = input('Please input file path and name:')
    decoded_msg = []
    try:
        with open(path, "r") as msg:
            for element in list(msg.read()):
                if element in decoder:
                    decoded_msg.append(alphabet[decoder.index(element)])
                else:
                    decoded_msg.append(element)
    except FileNotFoundError:
        print("Entered file is't insist")
    print(''.join(decoded_msg))

# we are coding
elif inp_key == "c":
    try:
        shift = int(input("Input shift to code: "))
    except ValueError:
        print('Shift should be int')
        exit()

    inp_msg = input("Input message: ")
    path = input('Please input file path and name:')
    coded_msg = []

    # carousel ... # carousel
    cursor = 0
    coder = alphabet[:]
    while cursor != shift:
        if shift < 0:
            coder.insert(0, coder.pop(len(coder) - 1))
            cursor -= 1
        elif shift > 0:
            coder.append(coder.pop(0))
            cursor += 1

    with open(path, "w") as msg:
        for element in inp_msg:
            if element in alphabet:
                coded_msg.append(coder[alphabet.index(element)])
            else:
                coded_msg.append(element)
        msg.write(''.join(coded_msg))

    print(''.join(coded_msg))

else:
    print("This program can code and decode information messages by using Caesar's coding algorithm \n"
          "Program accept 'c' for coding and 'd' for decoding")