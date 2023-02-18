n = int(input())
row = 1

even_set = set()
odd_set = set()
for _ in range(n):
    sum_name = 0
    name = input()
    for letter in name:
        sum_name += ord(letter)
    sum_name = sum_name // row
    if sum_name % 2 == 0:
        even_set.add(sum_name)
    else:
        odd_set.add(sum_name)
    row += 1

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)


if sum_even_set == sum_odd_set:
    print(*even_set.union(odd_set), sep=', ')
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=', ')
elif sum_even_set > sum_odd_set:
    print(*even_set.symmetric_difference(odd_set), sep=', ')
