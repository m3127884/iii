deck = []

for color in range(4):
    for number in range(13):
        card = (color, number)
        deck.append(card)

print(deck)
print(len(deck))
