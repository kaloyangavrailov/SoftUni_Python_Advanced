sequence_a = {int(x) for x in input().split()}
sequence_b = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    word_1_c, word_2_c, *numbers = input().split()
    numbers = [int(x) for x in numbers]
    if word_1_c + ' ' + word_2_c == 'Add First':
        sequence_a = sequence_a.union(set(numbers))
    elif word_1_c + ' ' + word_2_c == 'Add Second':
        sequence_b = sequence_b.union(set(numbers))
    elif word_1_c + ' ' + word_2_c == 'Remove First':
        sequence_a = sequence_a.difference(set(numbers))
    elif word_1_c + ' ' + word_2_c == 'Remove Second':
        sequence_b = sequence_b.difference(set(numbers))
    elif word_1_c + ' ' + word_2_c == 'Check Subset':
        if sequence_b.issubset(sequence_a) or sequence_a.issubset(sequence_b):
            print(True)
        else:
            print(False)

print(*sorted(sequence_a), sep=', ')
print(*sorted(sequence_b), sep=', ')