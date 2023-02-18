sequence_numbers = list(map(int,input().split()))
achieved_pairs = set()
target_number = int(input())

while sequence_numbers:
    for index_a in range(0,len(sequence_numbers.copy())-1):
        if sequence_numbers[index_a] >= target_number:
            sequence_numbers.pop(sequence_numbers[index_a])
            continue
        for index_b in range(index_a+1,len(sequence_numbers.copy())):
            if sequence_numbers[index_a] + sequence_numbers[index_b] == target_number:
                achieved_pairs.add(sequence_numbers[index_a])
                achieved_pairs.add(sequence_numbers[index_b])
                sequence_numbers.pop(sequence_numbers[index_a])
                sequence_numbers.pop(sequence_numbers[index_b])
                print(f'{sequence_numbers[index_a]} + {sequence_numbers[index_b]} = {target_number}')
