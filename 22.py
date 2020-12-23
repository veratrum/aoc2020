from aoc import aopen
from copy import deepcopy

with aopen(22) as f:
    decks = [[int(x) for x in deck.split('\n')[1:]] for deck in f.read().split('\n\n')]

def part1(_decks):
    decks = deepcopy(_decks)
    while True:
        if len(decks[0]) == 0 or len(decks[1]) == 0:
            full = decks[1] if len(decks[0]) == 0 else decks[0]

            result = 0
            for i, x in enumerate(full):
                result += (len(full) - i) * x
            print(result)
            break

        c1 = decks[0].pop(0)
        c2 = decks[1].pop(0)
        if c1 > c2:
            decks[0].extend((c1, c2))
        else:
            decks[1].extend((c2, c1))

def part2(_decks):
    decks = _decks

    alreadySeen = set()
    while True:
        if len(decks[0]) == 0:
            return False
        elif len(decks[1]) == 0:
            return True
        if (str(decks) in alreadySeen):
            return True
        alreadySeen.add(str(decks))

        c1 = decks[0].pop(0)
        c2 = decks[1].pop(0)
        if c1 <= len(decks[0]) and c2 <= len(decks[1]):
            __decks = deepcopy(decks)
            __decks[0] = __decks[0][:c1]
            __decks[1] = __decks[1][:c2]
            result = part2(__decks)
        else:
            result = c1 > c2
        
        if result:
            decks[0].extend((c1, c2))
        else:
            decks[1].extend((c2, c1))


_decks = deepcopy(decks)
part1(_decks)

_decks = deepcopy(decks)
result = part2(_decks)
full = _decks[1] if len(_decks[0]) == 0 else _decks[0]
result = 0
for i, x in enumerate(full):
    result += (len(full) - i) * x
print(result)