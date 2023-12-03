import re

file = 'input.txt'

fileContent = open("input/" + file, "r").read()
results = re.findall("[^\d]*(\d).*(\d)[^\d]*|[^\d]*(\d)[^\d]*", fileContent)

out = 0
for result in results:
    out += int(result[0] or 0) * 10 + int(result[1] or 0) + int(result[2] or 0) * 11

print('out', out)
