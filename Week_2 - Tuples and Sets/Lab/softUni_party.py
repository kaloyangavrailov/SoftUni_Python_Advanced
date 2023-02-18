n = int(input())
guest_list = [input() for _ in range(n)]
arrived_list = []

while True:
    command = input()
    if command == 'END':
        break
    else:
        arrived_list.append(command)

not_arrived_list = set(guest_list).difference(arrived_list)
print(len(not_arrived_list))
not_arrived_list = sorted(not_arrived_list)
for guest in not_arrived_list:
    print(guest)