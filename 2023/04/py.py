file = 'input.txt'

fileContent = open("input/" + file, "r").read()

lines = fileContent.split('\n')

out = 0
for card in lines:
    numbers = card.split(':')[1].split('|')
    winningNumbers = numbers[0].split()
    actualNumbers = numbers[1].split()

    wonNumbers = 0
    for num in actualNumbers:
        if num in winningNumbers:
            wonNumbers += 1
    if wonNumbers > 0:
        out += 2 ** (wonNumbers - 1)
print('out', out)
