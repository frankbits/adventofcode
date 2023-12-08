import re


def get_hand_type(cards):
    card_counts = {}
    for card in cards:
        card_counts[card] = card_counts.get(card, 0) + 1
    card_counts = dict(sorted(card_counts.items(), key=lambda item: -item[1]))

    card_counts_values = list(card_counts.values())
    match card_counts_values[0]:
        case 5:
            return 5
        case 4:
            return 4
        case 3:
            if card_counts_values[1] == 2:
                return 3.5  # full house
            else:
                return 3
        case 2:
            if card_counts_values[1] == 2:
                return 2.5  # double pair
            else:
                return 2
        case 1:
            return 1


file = 'input/input.txt'

lines = list(map(lambda line: line.split(), open(file, "r").readlines()))

hands = []
for line in lines:
    hand = re.findall(r".", line[0])
    bid = line[1]

    hands.append([hand, get_hand_type(hand), bid])

cardRanks = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}


def sort_hands(hand):
    sort_tuple = [hand[1]]
    for card in hand[0]:
        sort_tuple.append(int(cardRanks.get(card, card)))
    return sort_tuple


hands = sorted(hands, key=sort_hands)

out = 0
for i, hand in enumerate(hands):
    out += int(hand[2]) * (i + 1)
print('out', out)
