string = input()
lists = string.split('|')
final_lists = []
for lst in lists[::-1]:
    final_lists.extend(lst.split())

print(*final_lists, sep=' ')