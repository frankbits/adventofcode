import re

file = 'input/input.txt'

lines = list(map(lambda line: line.strip(), open(file, "r").readlines()))

direction_inputs = lines[0]

network = {}
for node_data in lines[2:]:
    directions = re.findall(r"(...) = \((...), (...)\)", node_data)[0]
    network[directions[0]] = {}
    network[directions[0]]['L'] = directions[1]
    network[directions[0]]['R'] = directions[2]

current_node = 'AAA'
i = 0
while current_node != 'ZZZ':
    direction_input = direction_inputs[i % len(direction_inputs)]
    current_node = network[current_node][direction_input]
    i += 1
print('out', i)
