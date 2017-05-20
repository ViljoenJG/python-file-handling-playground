def celsius_to_fahrenheit(celsius):
    if celsius > -273.15:
        return round(celsius * 1.8 + 32, 2)

output = open('results.txt', 'w')

with open('input.txt') as source:
    content = [float(i.rstrip('\n')) for i in source.readlines()]
    for c in content:
        fahrenheit = celsius_to_fahrenheit(c)
        if fahrenheit is not None:
            output.write(str(fahrenheit) + '\n')

output.close()
