def forecast(*args):

    forecast = args
    sorted_forecast = []
    sorted_forecast_sunny = []
    sorted_forecast_cloudy = []
    sorted_forecast_rainy = []
    print_list = []
    for el in forecast:
        if 'Sunny' in el[1]:
            sorted_forecast_sunny.append(el)
    sorted_forecast_sunny = sorted(sorted_forecast_sunny, key= lambda x: x[0])
    for el in forecast:
        if 'Cloudy' in el[1]:
            sorted_forecast_cloudy.append(el)
    sorted_forecast_cloudy = sorted(sorted_forecast_cloudy, key= lambda x: x[0])

    for el in forecast:
        if 'Rainy' in el[1]:
            sorted_forecast_rainy.append(el)
    sorted_forecast_rainy = sorted(sorted_forecast_rainy, key= lambda x: x[0])
    sorted_forecast = sorted_forecast_sunny + sorted_forecast_cloudy + sorted_forecast_rainy

    for el in sorted_forecast:
        print_list.append(f'{el[0]} - {el[1]}\n')
    return ''.join(print_list)
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))