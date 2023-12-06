import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


file = 'test.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

sections.pop(0)
seeds = chunk(sections.pop(0).split(), 2)
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

# seed_ranges = [(79, 14), (55, 13)]  # Example input
seed_ranges = seeds  # Example input

print('seed_ranges', seed_ranges)


def convert_range(source_range, map):
    print('source_range', source_range)
    start, length = source_range
    for map_range in map:
        map_start, source_start, map_length = map_range
        if int(start) >= int(source_start) and int(start) + int(length) <= int(source_start) + int(map_length):
            return (int(map_start) + int(start) - int(source_start), int(length))
    return source_range


print('maps', maps)
for map in maps:
    print('map', map)
    seed_ranges = [convert_range(range, map) for range in seed_ranges]
    print('seed_ranges', seed_ranges)

lowest_location_number = min(range[0] for range in seed_ranges)
print('lowest_location_number', lowest_location_number)
