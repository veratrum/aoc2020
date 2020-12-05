


with open('input\\5.txt', 'r') as f:
    positions = f.readlines()

twos = [2 ** i for i in range(7)]

def check(position):
    x = 0
    y = 0
    for i, c in enumerate(position[:7]):
        y += twos[6 - i] if c == 'B' else 0
    for i, c in enumerate(position[7:]):
        x += twos[2 - i] if c == 'R' else 0
    seatID = x + y * 8
    return seatID

best = 0
for position in positions:
    seatID = check(position)
    if seatID > best:
        best = seatID

print(best)

notFound = list(range(best + 1))
for position in positions:
    seatID = check(position)
    notFound.remove(seatID)
print(notFound[len(notFound) - 1])
