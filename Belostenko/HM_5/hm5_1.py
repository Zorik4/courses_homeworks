from string import ascii_letters as alphabet

while True:
    try:
        path = input('Path: ')
        file = open(path, 'r')
        break
    except FileNotFoundError:
        print('File not found')
        continue

content = list(file)
letters = list(alphabet)
words = []
count_dict = {}
count = 0

print('File: ', content)

for line in range(len(content)):
    word = list(content[line])
    for word_letter in range(len(word)):
        words.append(word[word_letter])

for count_alphabet in range(len(letters)):
    letter = letters[count_alphabet]
    for count_letter in range(len(words)):
        if letter == words[count_letter]:
            count += 1
        else:
            continue
    count_dict.update({letters[count_alphabet]:count})
    count = 0
print('Counted letters: ', count_dict)
