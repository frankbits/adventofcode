import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


file = 'test.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

sections.pop(0)
seeds = sections.pop(0).split()
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

conversionTable = {}
for i, conversionMap in enumerate(maps):
    print('conversionTable', conversionTable)
    for conversion in conversionMap:
        for conversionRange, conversionDifference in conversionTable.items():
            beforeIntersection = range(conversionRange[0], max((conversion[0]), conversionRange[0]))
            intersection = range(max((conversion[0]), conversionRange[0]),
                                 min(conversion[-1], conversionRange[-1]) + 1)
            afterIntersection = range(min(conversion[-1], conversionRange[-1] + 1),
                                      conversionRange[-1] + 1)

            if len(beforeIntersection):
                if conversion[0] <= conversionRange[0]:
                    conversionTable[beforeIntersection] = con

            conversionRangeNew = range(int(conversion[1]), int(conversion[1]) + int(conversion[2]))

            conversionDifferenceNew = int(conversion[0]) - int(conversion[1])
            conversionTables[i].update({conversionRange: conversionDifference})

print('conversionTables', conversionTables)

locations = []
print('seeds', seeds)
areas = []
for i, seed in enumerate(seeds):
    if i % 2 == 1:
        break
    seed = int(seed)
    print('seed', seed)
    for conversionTable in conversionTables:
        for conversionRange, conversionDifference in conversionTable.items():
            beforeIntersection = range(seed, max((conversionRange[0]), seed))
            intersection = range(max((conversionRange[0]), seed),
                                 min(conversionRange[-1], seed + int(seeds[i + 1]) - 1) + 1)
            afterIntersection = range(min(conversionRange[-1], seed + int(seeds[i + 1]) - 1),
                                      seed + int(seeds[i + 1]))
            print('intersection', intersection)
            print('len(intersection)', len(intersection))
            if len(intersection):
                areas.append(intersection)
                print('conversionRange', conversionRange)
                seed += conversionDifference
                # print('conversionDifference', conversionDifference)
                break
        # print('seedNew', seed)
    locations.append(seed)

print('locations', locations)
print('out', min(locations))
