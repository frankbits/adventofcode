import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def disjoint_segments(ranges):
    ranges.sort(key=lambda x: (x[0], -x[1]))
    # In order to get extra loop iteration, add one dummy range
    ranges.append((float("inf"), None, None))
    stack_end = []  # use separate stacks for ends, and data
    stack_data = []
    current = ranges[0][0]
    for start, end, data in ranges:
        # flush data from stack up to start - 1.
        while stack_end and stack_end[-1] < start:
            end2 = stack_end.pop()
            data2 = stack_data.pop()
            if current <= end2:
                yield current, end2, data2
                current = end2 + 1
        if stack_end and current < start:
            yield current, start - 1, stack_data[-1]
        # stack the current tuple's info
        current = start
        if not stack_end or stack_data[-1] != data or end > stack_end[-1]:
            stack_end.append(end)
            stack_data.append(data)

def merge(segments):
    start, end, data = next(segments)  # keep one segment buffered
    for start2, end2, data2 in segments:
        if end + 1 == start2 and data == data2:  # adjacent & same data
            end = end2  # merge
        else:
            yield start, end, data
            start, end, data = start2, end2, data2
    yield start, end, data  # flush the buffer


file = 'test.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

sections.pop(0)
seeds = sections.pop(0).split()
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

print('maps', maps)
for i, conversionMap in enumerate(maps):
    print('conversionMap', conversionMap)
    for j, conversion in enumerate(conversionMap):
        print('conversion', conversion)
        newTuple = []
        for k, num in enumerate(conversion):
            print('num', num)
            newTuple.append(int(num))
            print('num', num)
        conversionMap[j] = tuple(newTuple)
        print('conversion', conversion)
    maps[i] = conversionMap
    print('conversionMap', conversionMap)
print('maps', maps)

for i, conversionMap in enumerate(maps):
    print('conversionMap', conversionMap)
    print('list(merge(disjoint_segments(maps)))', list(merge(disjoint_segments(conversionMap))))
