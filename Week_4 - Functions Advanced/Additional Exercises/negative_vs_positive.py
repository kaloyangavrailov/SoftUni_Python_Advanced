def func(lst):
    lst_neg = [int(el) for el in lst if int(el) < 0]
    lst_pos = [int(el) for el in lst if int(el) > 0]

    print(sum(lst_neg))
    print(sum(lst_pos))
    if abs(sum(lst_neg)) > sum(lst_pos):
        return f'The negatives are stronger than the positives'
    else:
        return f'The positives are stronger than the negatives'

print(func(input().split()))