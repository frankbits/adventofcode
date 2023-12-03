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


maxNumbers = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

out = 0
for i, game in enumerate(games):
    for colorSet in game:
        if int(colorSet[0]) > maxNumbers[colorSet[1]]:
            break
    else:
        out = out + i + 1

print('out', out)
