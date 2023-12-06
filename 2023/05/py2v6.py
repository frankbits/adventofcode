import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def disjoint_segments(range1, range2):
    beforeIntersection = range(min(range2[0], range1[0]), min(min(range2[-1], range1[-1]), max(range2[0], range1[0])) + 1)
    intersection = range(max(range2[0], range1[0]),
                         min(range2[-1], range1[-1]) + 1)
    afterIntersection = range(max(min(range2[-1], range1[-1]), max(range2[0], range1[0])),
                              max(range2[-1], range1[-1]) + 1)

    return beforeIntersection, intersection, afterIntersection


def change_conversion_format(conversion):
    conversion_range = range(int(conversion[1]), int(conversion[1]) + int(conversion[2]))
    conversion_difference = int(conversion[0]) - int(conversion[1])
    return {conversion_range: conversion_difference}


def intersect_conversions(conversion1, conversion2):
    if len(conversion1) > 2:
        # print('1')
        conversion1_range = range(int(conversion1[1]), int(conversion1[1]) + int(conversion1[2]))
        conversion1_difference = int(conversion1[0]) - int(conversion1[1])
    else:
        conversion1_range = conversion1[0]
        conversion1_difference = int(conversion1[1])

    # print('conversion2TEST', conversion2)
    if len(conversion2) > 2:
        # print('2')
        conversion2_range = range(int(conversion2[1]), int(conversion2[1]) + int(conversion2[2]))
        conversion2_difference = int(conversion2[0]) - int(conversion2[1])
    else:
        conversion2_range = conversion2[0]
        conversion2_difference = int(conversion2[1])

    before_intersection, intersection, after_intersection = disjoint_segments(conversion1_range, conversion2_range)

    intersectedConversions = []
    if len(before_intersection):
        if conversion1_range[0] < conversion2_range[0]:
            lower_bounds = conversion1_difference
        else:
            lower_bounds = conversion2_difference
        intersectedConversions.append((before_intersection, lower_bounds))

    if len(intersection):
        intersectedConversions.append((intersection, conversion1_difference + conversion2_difference))

    if len(after_intersection):
        if conversion1_range[-1] > conversion2_range[-1]:
            upper_bounds = conversion1_difference
        else:
            upper_bounds = conversion2_difference
        intersectedConversions.append((after_intersection, upper_bounds))

    return intersectedConversions


def merge(segments):
    start, end, data = next(segments)  # keep one segment buffered
    for start2, end2, data2 in segments:
        if end + 1 == start2 and data == data2:  # adjacent & same data
            end = end2  # merge
        else:
            yield start, end, data
            start, end, data = start2, end2, data2
    yield start, end, data  # flush the buffer


file = 'input.txt'

fileContent = open("input/" + file, "r").read()

sections = re.split(r".+:\s", fileContent)

sections.pop(0)
seeds = sections.pop(0).split()
maps = list(map(lambda section: list(chunk(section.split(), 3)), sections))

# print('maps', maps)
conversionsTable = {}
for i, conversionMap in enumerate(maps):
    # print('conversionMap', conversionMap)
    conversionsTableTmp = conversionsTable.copy()
    # print('conversionsTableTmp', conversionsTableTmp)
    for j, conversion in enumerate(conversionMap):
        # print('conversion', conversion)
        # print('conversionsTableTmp', conversionsTableTmp)
        for conversion2 in conversionsTableTmp.items():
            # print('conversion2', conversion2)
            intersectedConversions = intersect_conversions(conversion, conversion2)
            # TODO: problem before/after intersection gets added without being checked against other ranges
            # print('intersectedConversions', intersectedConversions)
            conversionsTable.update(intersectedConversions)
        if not len(conversionsTableTmp):
            conversionsTable.update(change_conversion_format(conversion))
    # conversionsTable = conversionsTableTmp.copy()
    # print('conversionsTable', conversionsTable)
conversionsTable = sorted(conversionsTable.items(), key=lambda conversion_range: conversion_range[0][0])
print('conversionsTable', conversionsTable)
print('len(conversionsTable)', len(conversionsTable))

locations = []
for seed in seeds:
    print('seed', seed)
    for conversionRange, conversionDifference in conversionsTable:
        print('conversionRange', conversionRange)
        if seed in conversionRange:
            seed = seed + conversionDifference
            break
    locations.append(seed)
    print('locations', locations)
print('locations', locations)
print('out', min(locations))
