n = int(input())
car_lot = set()

for iteration in range(n):
    command, car = input().split(', ')
    if command == 'IN':
        car_lot.add(car)
    else:
        if car in car_lot:
            car_lot.remove(car)
if car_lot:
    {print(item) for item in car_lot}
else:
    print(f'Parking Lot is Empty')