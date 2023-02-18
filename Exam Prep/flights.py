def flights(*args):
    lst = args
    d = {}
    for i in range(0 ,len(lst), 2):
        if lst[i] == 'Finish':
            break
        else:
            if lst[i] not in d:
                d[lst[i]] = lst[i+1]
            elif lst[i] in d:
                d[lst[i]] += lst[i + 1]
    return d

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))