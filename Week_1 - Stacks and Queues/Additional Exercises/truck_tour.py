from collections import deque

number_of_pumps = int(input())
route = deque()
tank = 0
for pump in range(number_of_pumps):
    route.append(list(map(int, input().split())))

route_copy = route.copy()

station_counter = 0

while route_copy:
    gas_station = route_copy.popleft()
    if station_counter == 0:
        starting_station = gas_station
    tank += gas_station[0]
    if tank >= gas_station[1]:
        station_counter = 1
        tank -= gas_station[1]
        continue
    else:
        route.append(gas_station)
        tank = 0
        station_counter = 0
        continue

print(route.index(starting_station))