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
            symbols.append({'line': i, 'span': result.span()})

partNumbers = []
partNumbersSum = 0
for number in numbers:
    lineNumber = number['line']
    for symbol in symbols:
        if lineNumber - 1 <= symbol['line'] <= lineNumber + 1 and (
                 number['span'][0] <= symbol['span'][0] <= number['span'][1] or
                 number['span'][0] <= symbol['span'][1] <= number['span'][1]):
            # print('partNumber', number['number'])
            partNumbers.append(number['number'])
            partNumbersSum = partNumbersSum + number['number']

print(partNumbers)
print(partNumbersSum)
