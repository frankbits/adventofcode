import re

file = "input.txt"

fileContent = open("input/" + file, "r").read()

numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

matches = re.finditer('(?=(' + '|'.join(numbers) + '))', fileContent)
inserted = 0
for match in matches:
    matchString = match.group(1)
    digit = numbers.index(matchString)
    insertAt = match.span()[0] + inserted
    fileContent = fileContent[:insertAt] + str(digit) + fileContent[insertAt:]
    inserted = inserted + 1

# lines = fileContent.split('\n')
#
# out = 0
# for i, line in enumerate(lines):
#
#     matches = re.search("[^\d]*(\d).*(\d)[^\d]*|[^\d]*(\d)[^\d]*", line)
#     numbersInLine = matches.groups() if matches else None
#
#     firstDigit = 0
#     secondDigit = 0
#
#     if numbersInLine:
#         firstDigit = int(numbersInLine[0] or numbersInLine[2] or 0)
#         secondDigit = int(numbersInLine[1] or numbersInLine[2] or 0)
#
#     out += firstDigit * 10 + secondDigit

results = re.findall("[^\d]*(\d).*(\d)[^\d]*|[^\d]*(\d)[^\d]*", fileContent)

out = 0
for result in results:
    out += int(result[0] or 0) * 10 + int(result[1] or 0) + int(result[2] or 0) * 11

print('out', out)
