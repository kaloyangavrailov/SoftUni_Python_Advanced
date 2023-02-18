def math_operations(*args, **kwargs):
    numbers = args
    keys = list(kwargs.keys())
    for i in range(len(numbers)):
        if keys[i%4] == 'a':
            kwargs[keys[i%4]] += numbers[i]
        elif keys[i%4] == 's':
            kwargs[keys[i%4]] -= numbers[i]
        elif keys[i % 4] == 'd':
            if numbers[i] == 0:
                continue
            else:
                kwargs[keys[i % 4]] /= numbers[i]
        elif keys[i % 4] == 'm':
            kwargs[keys[i % 4]] *= numbers[i]
    kwargs = sorted(kwargs.items(), key =lambda x: (-x[1], x[0]))
    result = []
    for el in kwargs:
        result.append(f'{el[0]}: {el[1]:.1f}')
    return '\n'.join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))