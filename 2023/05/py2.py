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

# conversionTable = {}
# for conversionMap in maps:
#     for conversion in conversionMap:
#         print('conversionTable', conversionTable)
#         for i, conversion2 in conversionTable.items():
#             if i <= int(conversion[1]) <= (i + conversion2[0]):
#                 print('conversion[1]', conversion[1])
#                 print('i', i)
#                 conversionTable[i] = int(conversion[0]) - int(conversion[1])
#         conversionTable.setdefault(int(conversion[1]), int(conversion[0]) - int(conversion[1]))
#         conversionTable.setdefault(int(conversion[1]) + int(conversion[2]) - 1, int(conversion[0]) - int(conversion[1]))

conversionTable = {}
for conversionMap in maps:
    for conversion in conversionMap:
        print('conversionTable', conversionTable)
        conversionTableNew = conversionTable.copy()
        conversionRangeNew = range(int(conversion[1]), int(conversion[1]) + int(conversion[2]))
        for conversionRange, conversionDifference in conversionTable.items():
            intersection = range(max(conversionRange[0], conversionRangeNew[0]),
                                 min(conversionRange[-1], conversionRangeNew[-1]) + 1)
            print('conversionRange', conversionRange)
            print('conversionRangeNew', conversionRangeNew)
            print('intersection', intersection)
            # print('conversionDifference', conversionDifference)
            rangeStart = conversionRange[0]
            # print('rangeStart', rangeStart)
            rangeEnd = conversionRange[-1]
            # print('rangeEnd', rangeEnd)
            if int(conversion[1]) in conversionRange:
                del conversionTableNew[conversionRange]
                conversionTableNew[range(rangeStart, int(conversion[1]) - 1)] = conversionDifference
                conversionTableNew[range(int(conversion[1]), int(conversion[1]) + int(conversion[2]))] = (
                        conversionDifference + int(conversion[0]) - int(conversion[1])
                )
                conversionTableNew[range(int(conversion[1]) + int(conversion[2]), rangeEnd)] = conversionDifference
        conversionTable = conversionTableNew.copy()
        conversionTable.setdefault(
            range(int(conversion[1]), int(conversion[1]) + int(conversion[2])), int(conversion[0]) - int(conversion[1]))

    print('conversionTable', conversionTable)

    # locations = []
    # for seed in seeds:
    #     for conversionTable in conversionTables:
    #         if int(seed) in conversionTable:
    #             seed = conversionTable[int(seed)]
    #     locations.append(seed)

    # locations = []
    # # print('seeds', seeds)
    # for i, seedStart in enumerate(seeds):
    #     # print('i', i)
    #     # print('seedStart', seedStart)
    #     if i % 2 == 0:
    #         # print('range(int(seed), int(seeds[i + 1]))', range(int(seedStart), int(seedStart) + int(seeds[i + 1])))
    #         for seed in range(int(seedStart), int(seedStart) + int(seeds[i + 1])):
    #             # print('seed', seed)
    #             for conversionMap in maps:
    #                 for conversion in conversionMap:
    #                     minIndex = int(conversion[1])
    #                     maxIndex = int(conversion[1]) + int(conversion[2]) - 1
    #                     if minIndex <= int(seed) <= maxIndex:
    #                         seed = int(conversion[0]) + int(seed) - minIndex
    #                         break
    #             locations.append(seed)

    # print('locations', locations)
    # print('out', min(locations))
