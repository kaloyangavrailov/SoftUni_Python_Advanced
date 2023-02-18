n = int(input())
empty_set = set()
for iteration in range(n):
    empty_set.add(input())

for item in empty_set.copy():
    print(empty_set.pop())