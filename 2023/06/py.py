import re
from itertools import islice


def getDistanceFromButtonTime(btn_time, race_time):
    return (race_time - btn_time) * btn_time


file = 'input/input.txt'

lines = open(file, "r").readlines()


times = re.findall(r"\d+", lines[0])
distances = re.findall(r"\d+", lines[1])

print('times', times)
print('distances', distances)

out = 1
for i, time in enumerate(times):
    time = int(time)
    distance = int(distances[i])

    newDistances = []
    for btn_time in range(1, time):
        newDistance = getDistanceFromButtonTime(btn_time, time)
        if newDistance > distance:
            newDistances.append(newDistance)
    print('len(newDistances)', len(newDistances))
    out *= len(newDistances)

print('out', out)
