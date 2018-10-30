import random
from string import ascii_letters as letters
dict_list = logins = passwords = []
dictionary = {}
for i in range(10):
    length = random.randint(1, 10)
    logins = (random.sample(letters, length))
    logins = "".join(logins)
    passwords = str(random.randint(1000, 1000000))
    dict_list = {logins:passwords}
    dictionary.update(dict_list)
print(dictionary)
check = input("Check login in dict: ")
if check in dictionary:
    print("Login found, password: ", dictionary[check])
else:
    print("Login not found, creating new login")
    pass_new = input('Password: ')
    dictionary.update({check:pass_new})
    print(dictionary)


