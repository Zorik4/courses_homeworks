import random
import string
import os

user_choice = input('Make a choice: 1.Encryption or 2.Decryption\n')

if user_choice == '1':
    key_for_encrypt = random.randint(1, 10)
    print('Shift = {}'.format(key_for_encrypt))
    user_text = input('What do you want encrypt?\n')
    encryption = ''
    for element in user_text:
        encryption += (string.ascii_letters[
                         string.ascii_letters.index(element) + key_for_encrypt])
    print(encryption)
    with open('encryption.txt', 'w') as file:
        file.write(encryption)
        print(os.path.split(os.path.abspath('encryption.txt')))
    exit()
elif user_choice == '2':
    key_for_decrypt = int(input('How much to move?\n'))
    path_file = input('The path to file:\n')
    decryption = ''
    with open(path_file, 'r') as crypt_file:
        crypt_file = crypt_file.read()
    for element in crypt_file:
        decryption += (string.ascii_letters[
                         string.ascii_letters.index(element) - key_for_decrypt])
    print(decryption)
