import os

path=os.path.join(os.path.dirname(__file__), 'input.txt')
with open(path, 'r') as file:
    data=file.readlines()

def read(data):
    row=[]
    for line in data:
        hand,bid=line.strip().split()
        row.append((hand, int(bid)))
    return row

def value(hand):
    values = {
        'A':14,     'K':13,     'Q':12,     'J':1,      'T':10,
        '9':9,      '8':8,      '7':7,      '6':6,      '5':5,
        '4':4,      '3':3,      '2':2,
        }
    return [values[card] for card in hand]

def findTypeJoker(hand):
    count={card: hand.count(card) for card in set(hand)}
    joker=count.get('J', 0)
    topType=7
    for card in 'AKQT98765432':
        jokerHand=hand
        for _ in range(joker):
            jokerHand = jokerHand.replace('J', card, 1)
        newType=findType(jokerHand)
        topType=min(topType, newType)
    return topType

def findType(hand):
    count={card: hand.count(card) for card in set(hand)}
    counts=sorted(count.values(), reverse=True)
    types=[0,1,2,3,4,5,6]
    if counts[0]==5: return types[0]                   # Five of a kind
    if counts[0]==4: return types[1]                   # Four of a kind
    if counts[0]==3 and counts[1]==2: return types[2]  # Full house
    if counts[0]==3: return types[3]                   # Three of a kind
    if counts[0]==2 and counts[1]==2: return types[4]  # Two pairs
    if counts[0]==2: return types[5]                   # One pair
    return types[6]                                    # High card

total=read(data)
total.sort(key=lambda x: (findTypeJoker(x[0]), *[-value(x[0])[i] for i in range(5)]))
winnings=0

for i, (hand,bid) in enumerate(reversed(total)):
    rank=i+1
    winnings+=rank*bid
    print(f"Hand: {hand}, Rank: {rank}, Bid: {bid}, Winnings: {rank*bid}")

print(f"Total: {winnings}")
