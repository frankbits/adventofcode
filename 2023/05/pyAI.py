import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def parse_input(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
        # lines = file.readlines()

    print('file_content', file_content)
    sections = re.split(r".+:\s", file_content)[1:]

    print('sections', sections)

    # print(lines) # Add this line to print out the lines

    seeds = sections.pop(0).split()

    print('seeds', seeds)


    # seeds = list(map(int, lines[0].split()[1:]))
    #
    # print('seeds', seeds)

    # print('lines[i+2:i+6]', lines[1 + 2:1 + 6])

    # mappings = {}
    # for i in range(1, 8):
    #     mappings[f'{lines[i].split()[0]}_to_{lines[i+1].split()[0]}_map'] = [tuple(map(int, line.split())) for line in lines[i+2:i+6]]

    mappings = list(map(lambda section: list(chunk(section.split(), 3)), sections))

    return seeds, mappings

seeds, mappings = parse_input('input/test.txt')

def map_value(value, mapping):
    for dest_start, start, length in mapping:
        end = start + length
        print('start, end, dest_start', start, end, dest_start)
        if int(start) <= int(value) < int(end):
            return int(dest_start) + (int(value) - int(start))
    return value

def lowest_location_number(seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location, seeds):
    min_location = float('inf')
    for seed in seeds:
        soil = map_value(seed, seed_to_soil)
        fertilizer = map_value(soil, soil_to_fertilizer)
        water = map_value(fertilizer, fertilizer_to_water)
        light = map_value(water, water_to_light)
        temperature = map_value(light, light_to_temperature)
        humidity = map_value(temperature, temperature_to_humidity)
        location = map_value(humidity, humidity_to_location)
        min_location = min(min_location, location)
    return min_location

def lowest_location_number_part_two(seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location, seed_ranges):
    min_location = float('inf')
    for start, length in seed_ranges:
        for seed in range(int(start), int(start) + int(length)):
            soil = map_value(seed, seed_to_soil)
            fertilizer = map_value(soil, soil_to_fertilizer)
            water = map_value(fertilizer, fertilizer_to_water)
            light = map_value(water, water_to_light)
            temperature = map_value(light, light_to_temperature)
            humidity = map_value(temperature, temperature_to_humidity)
            location = map_value(humidity, humidity_to_location)
            min_location = min(min_location, location)
    return min_location


print('mappings', mappings)

# print(lowest_location_number(mappings['seed_to_soil_map'], mappings['soil_to_fertilizer_map'], mappings['fertilizer_to_water_map'], mappings['water_to_light_map'], mappings['light_to_temperature_map'], mappings['temperature_to_humidity_map'], mappings['humidity_to_location_map'], seeds))
print(lowest_location_number(mappings[0], mappings[1], mappings[2], mappings[3], mappings[4], mappings[5], mappings[6], seeds))

# print(lowest_location_number_part_two(mappings['seed_to_soil_map'], mappings['soil_to_fertilizer_map'], mappings['fertilizer_to_water_map'], mappings['water_to_light_map'], mappings['light_to_temperature_map'], mappings['temperature_to_humidity_map'], mappings['humidity_to_location_map'], [(79, 14), (55, 13)]))
print(lowest_location_number_part_two(mappings[0], mappings[1], mappings[2], mappings[3], mappings[4], mappings[5], mappings[6], chunk(seeds, 2)))
