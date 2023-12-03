import re

file = 'input.txt'

fileContent = open("input/" + file, "r").read()

lines = fileContent.split('\n')

numbers = []
symbols = []
for i, line in enumerate(lines):
    results = re.finditer(r"\d+|[^.\s]", line)

    for result in results:
        if result.group().isnumeric():
            numbers.append({'number': int(result.group()), 'line': i, 'span': result.span()})
        else:
            symbols.append({'symbol': result.group(), 'line': i, 'span': result.span()})

gears = []
gearRatioSum = 0
for symbol in symbols:
    lineNumber = symbol['line']
    if symbol['symbol'] == '*':
        adjacentNumbers = []
        for number in numbers:
            if lineNumber - 1 <= number['line'] <= lineNumber + 1 and (
                     number['span'][0] <= symbol['span'][0] <= number['span'][1] or
                     number['span'][0] <= symbol['span'][1] <= number['span'][1]):
                adjacentNumbers.append(number['number'])
        if len(adjacentNumbers) == 2:
            gears.append(symbol)
            gearRatioSum = gearRatioSum + adjacentNumbers[0] * adjacentNumbers[1]

print(gears)
print(gearRatioSum)
