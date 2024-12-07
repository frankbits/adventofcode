import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


file = 'input.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

# Remove the first empty element
sections.pop(0)

# Get the seeds
seeds = sections.pop(0).split()
print('seeds', seeds)

# Get the seed ranges
seedRanges = []
for i, seedStart in enumerate(seeds):
    if i % 2 != 0:
        continue
    seedEnd = int(seedStart) + int(seeds[i + 1]) - 1
    seedRanges.append([int(seedStart), seedEnd])
print('seedRanges', seedRanges)

# Get the conversion maps
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

locations = []
for conversionMap in maps:
    print('seedRanges', seedRanges)
    print('conversionMap', conversionMap)
    for i in range(len(seedRanges)):
        seedRange = seedRanges[i]
        print('seedRange', seedRange)
        seedStart = int(seedRange[0])
        seedEnd = int(seedRange[1])
        newStart = None
        newEnd = None

        for conversion in conversionMap:
            found = False
            sourceStart = int(conversion[1])
            sourceEnd = int(conversion[1]) + int(conversion[2]) - 1
            destinationStart = int(conversion[0])
            destinationEnd = int(conversion[0]) + int(conversion[2]) - 1

            if sourceStart <= seedStart <= sourceEnd:
                seedRange[0] = destinationStart + seedStart - sourceStart
                found = True
            elif seedStart <= sourceStart <= seedEnd:
                seedRange[1] = destinationStart - 1
                seedRange = [destinationStart, seedEnd]
                seedRanges.append(seedRange)
                found = True

            if sourceStart <= seedEnd <= sourceEnd:
                seedRange[1] = destinationStart + seedEnd - sourceStart
                found = True
            elif seedStart <= sourceEnd <= seedEnd:
                seedRange[1] = destinationEnd
                seedRanges.append([destinationEnd + 1, seedEnd])
                found = True

            if found:
                break

print('seedRanges', seedRanges)
print('out', min(seedRanges, key=lambda x: x[0])[0])
