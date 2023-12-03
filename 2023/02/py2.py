import re

file = "input.txt"

fileContent = open("input/" + file, "r").read()

results = re.findall(r"(\d+) ([a-zA-Z]+)([,;]|$)", fileContent, re.MULTILINE)

games = []
game = []
for result in results:
    game.append([result[0], result[1]])

    # if result[2] == ';' or not result[2]:
    if not result[2]:
        games.append(game)
        game = []

out = 0
for i, game in enumerate(games):
    maxNumbers = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for colorSet in game:
        if int(colorSet[0]) > maxNumbers[colorSet[1]]:
            maxNumbers[colorSet[1]] = int(colorSet[0])

    print(maxNumbers)
    out = out + maxNumbers['red'] * maxNumbers['green'] * maxNumbers['blue']

print('out', out)
