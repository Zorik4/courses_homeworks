import os

name = os.path.basename(__file__)
with open(name, 'r') as file:
    file = file.read()

print(file)
