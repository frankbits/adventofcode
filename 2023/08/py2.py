import re

file = 'input/test3.txt'

lines = list(map(lambda line: line.strip(), open(file, "r").readlines()))
# print('lines', lines)

direction_inputs = lines[0]

# print('direction_inputs', direction_inputs)

network = {}
current_nodes = []
for node_data in lines[2:]:
    # print('node_data', node_data)
    directions = re.findall(r"(...) = \((...), (...)\)", node_data)[0]
    # print('directions', directions)
    network[directions[0]] = {}
    network[directions[0]]['L'] = directions[1]
    network[directions[0]]['R'] = directions[2]

    if directions[0].endswith('A'):
        current_nodes.append(directions[0])
print('network', network)
print('current_nodes', current_nodes)

# i = 0
# end_reached = False
# while not end_reached:
#     for n, current_node in enumerate(current_nodes):
#         direction_input = direction_inputs[i % len(direction_inputs)]
#         current_nodes[n] = network[current_node][direction_input]
#     # print('current_nodes', current_nodes)
#     i += 1
#     # print('i', i)
#     # print([x for x in current_nodes if not x.endswith('Z')][:1])
#     print('current_nodes', current_nodes)
#     if not next((x for x in current_nodes if not x.endswith('Z'))):
#         end_reached = True
#
# print('out', i)

i = 0
end_reached = False
visited_nodes = {}
for n, current_node in enumerate(current_nodes):
    start_node = current_node
    network[start_node]['end'] = []
    print('current_nodeOUTER', current_node)
    while True:
        direction_input = direction_inputs[i % len(direction_inputs)]
        current_node = network[current_node][direction_input]
        i += 1

        print('direction_input', direction_input)
        print('current_node', current_node)
        if current_node.endswith('Z'):
            network[start_node]['end'].append(i)
        print('visited_nodes', visited_nodes)
        if direction_input in visited_nodes.get(current_node, []):
            network[start_node]['repeat'] = i
            break
        visited_nodes.setdefault(current_node, [])
        visited_nodes[current_node].append(direction_input)


print('network', network)

print('out', i)
