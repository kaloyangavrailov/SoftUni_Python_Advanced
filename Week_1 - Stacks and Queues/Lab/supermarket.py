from _collections import deque

list_customers = deque()

while True:
    input_info = input()
    if input_info == 'Paid':
        while list_customers:
            print(list_customers.popleft())
    elif input_info == 'End':
        print(f'{len(list_customers)} people remaining.')
        break
    else:
        list_customers.append(input_info)