file = 'input.txt'

fileContent = open("input/" + file, "r").read()

lines = fileContent.split('\n')

out = 0
wonNumbers = {}
cardCount = {}
for cardNum, card in enumerate(lines):
    wonNumbers.setdefault(cardNum, 0)
    cardCount.setdefault(cardNum, 1)

    numbers = card.split(':')[1].split('|')
    winningNumbers = numbers[0].split()
    actualNumbers = numbers[1].split()

    for num in actualNumbers:
        if num in winningNumbers:
            wonNumbers[cardNum] += 1
    for i in range(wonNumbers[cardNum]):
        cardCount.setdefault(cardNum + i + 1, 1)
        cardCount[cardNum + i + 1] += cardCount[cardNum]
    out += cardCount[cardNum]

print('wonNumbers', wonNumbers)
print('cardCount', cardCount)
print('out', out)
