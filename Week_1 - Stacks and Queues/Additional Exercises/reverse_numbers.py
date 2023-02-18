string_int = list(map(int, input().split()))

for index in range(len(string_int.copy())-1,-1,-1):
    print(string_int.pop(index), end=' ')