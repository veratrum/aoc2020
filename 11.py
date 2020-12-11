from aoc import aopen
from copy import deepcopy

with aopen(11) as f:
    seats = [list(x) for x in f.read().split('\n')]

def inRange(x, y, seats):
    return 0 <= x < len(seats) and 0 <= y < len(seats[0])

def stringSeats(seats):
    return '\n' + '\n'.join([''.join(x) for x in seats])

def countAdjacent(i, j, seats):
    adjacent = 0
    for k in range(i - 1, i + 2):
        if not inRange(k, 0, seats):
            continue
        for l in range(j - 1, j + 2):
            if not inRange(0, l, seats):
                continue
            if i == k and j == l:
                continue
            adjacent += 1 if seats[k][l] == '#' else 0
    return adjacent

def countVisible(i, j, seats):
    visible = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0:
                continue
            x = 1
            while inRange(i + k * x, j + l * x, seats):
                if seats[i + k * x][j + l * x] == '#':
                    visible += 1
                    break
                elif seats[i + k * x][j + l * x] == 'L':
                    break
                x += 1
    return visible

def tick(seats, nearbyFunction, nearbyThreshold):
    newSeats = deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            nearby = nearbyFunction(i, j, seats)
            if seat == 'L' and nearby == 0:
                seat = '#'
            elif seat == '#' and nearby >= nearbyThreshold:
                seat = 'L'
            newSeats[i][j] = seat
    return newSeats

originalSeats = deepcopy(seats)
for nearbyFunction, nearbyThreshold in [(countAdjacent, 4), (countVisible, 5)]:
    seats = deepcopy(originalSeats)
    while True:
        newSeats = tick(seats, nearbyFunction, nearbyThreshold)
        if stringSeats(newSeats) == stringSeats(seats):
            print(stringSeats(seats).count('#'))
            break
        seats = newSeats

