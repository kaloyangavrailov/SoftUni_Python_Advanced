from collections import deque


def word_checker(items_dict, letter_a, letter_b, items_list, flag, found_items_list):
    for item in items_list:
        for letter in (letter_a, letter_b):
            manipulate_string = list(item)
            for iteration in range(item.count(letter)):
                letter_index = manipulate_string.index(letter)
                items_dict[item][letter_index] = letter
                manipulate_string.remove(letter)
                manipulate_string.insert(letter_index, '-')
    for value in items_dict.values():
        if '*' not in value:
            flag = True
            found_items_list = ''.join(value)
            return items_dict, flag, found_items_list
        else:
            flag = False
    return items_dict, flag, found_items_list



words_ = {'rose': ['*', '*', '*', '*'],
          'tulip': ['*', '*', '*', '*', '*'],
          'lotus': ['*', '*', '*', '*', '*'],
          'daffodil': ['*', '*', '*', '*', '*', '*', '*', '*']
          }

found_word = ''

found_word_flag = False

words_list = list(words_.keys())

vowels = deque(input().split())  # first

consonants = deque(input().split())  # last

while not found_word and vowels and consonants:
    vowel, consonant = vowels.popleft(), consonants.pop()
    words_, found_word_flag, found_word = word_checker(words_, vowel, consonant, words_list, found_word_flag, found_word)

if found_word_flag:
    print(f"Word found: {found_word}")
else:
    print(f'Cannot find any word!')
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")