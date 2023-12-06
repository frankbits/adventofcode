import re


def get_distance_from_button_time(btn_time, race_time):
    return (race_time - btn_time) * btn_time


file = 'input/input.txt'

lines = open(file, "r").readlines()


time = ''.join(re.findall(r"\d+", lines[0]))
distance = ''.join(re.findall(r"\d+", lines[1]))

print('time', time)
print('distance', distance)

out = 1
time = int(time)
distance = int(distance)

newDistances = []
for btn_time in range(1, time):
    newDistance = get_distance_from_button_time(btn_time, time)
    if newDistance > distance:
        newDistances.append(newDistance)
out = len(newDistances)

print('out', out)
