def words_sorting(*args):
    word_dic = {}
    for word in args:
        ascii_value = 0
        for letter in word:
            ascii_value += ord(letter)
        word_dic[word] = ascii_value
    if sum(word_dic.values()) % 2 == 0:
        word_dic = sorted(word_dic.items(), key=lambda x: x[0])
    else:
        word_dic = sorted(word_dic.items(), key=lambda x: -x[1] )
    print_list = []

    for el in word_dic:
        print_list.append(f'{el[0]} - {el[1]}\n')
    return ''.join(print_list)
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))