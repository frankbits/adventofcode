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

conversionTables = []
for i, conversionMap in enumerate(maps):
    # print('conversionTables', conversionTables)
    conversionTables.append({})
    for conversion in conversionMap:
        conversionRange = range(int(conversion[1]), int(conversion[1]) + int(conversion[2]))
        conversionDifference = int(conversion[0]) - int(conversion[1])
        conversionTables[i].update({conversionRange: conversionDifference})

print('conversionTables', conversionTables)

locations = []
for i, seedStart in enumerate(seeds):
    if i % 2 == 1:
        break
    print('seedStart', seedStart)
    for seed in range(int(seedStart), int(seedStart) + int(seeds[i+1])):
        seed = int(seed)
        print('seed', seed)
        for conversionTable in conversionTables:
            for conversionRange, conversionDifference in conversionTable.items():
                if seed in conversionRange:
                    seed += conversionDifference
                    # print('conversionRange', conversionRange)
                    # print('conversionDifference', conversionDifference)
                    break
            # print('seedNew', seed)
        locations.append(seed)

print('locations', locations)
print('out', min(locations))
