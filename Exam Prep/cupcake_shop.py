def stock_availability(*args):
    inventory, commands = args[0], args[1::]
    if commands[0] == 'delivery':
        for i in range(1,len(commands)):
            inventory.append(commands[i])
    elif commands[0] == 'sell':
        if len(commands) == 2 and isinstance(commands[1], int):
            num = int(commands[1])
            for iteration in range(num):
                inventory.remove(inventory[0])
        elif len(commands) >= 2:
            for i in range(1, len(commands)):
                flavor = commands[i]
                if flavor in inventory:
                    for iteration in range(inventory.count(flavor)):
                        inventory.remove(flavor)
        elif len(commands) == 1:
            inventory.remove(inventory[0])
    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
