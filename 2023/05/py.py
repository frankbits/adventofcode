import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


file = 'input.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

sections.pop(0)
seeds = sections.pop(0).split()
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

# conversionTables = []
# for i, conversionMap in enumerate(maps):
#     conversionTables.append({})
#     for conversion in conversionMap:
#         for x in range(int(conversion[2])):
#             conversionTables[i].setdefault(int(conversion[1]) + x, int(conversion[0]) + x)
#
# print('conversionTables', conversionTables)
#
# locations = []
# for seed in seeds:
#     for conversionTable in conversionTables:
#         if int(seed) in conversionTable:
#             seed = conversionTable[int(seed)]
#     locations.append(seed)

locations = []
for seed in seeds:
    for conversionMap in maps:
        for conversion in conversionMap:
            minIndex = int(conversion[1])
            maxIndex = int(conversion[1]) + int(conversion[2]) - 1
            if minIndex <= int(seed) <= maxIndex:
                seed = int(conversion[0]) + int(seed) - minIndex
                break
    locations.append(seed)

print('locations', locations)
print('out', min(locations))
