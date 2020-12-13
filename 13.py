from aoc import aopen

with aopen(13) as f:
    depart, buses = f.readlines()
    depart = int(depart)
    buses = [int(x) if x != 'x' else -1 for x in buses.split(',')]

def part1():
    x = depart
    while True:
        targetBus = -1
        for bus in buses:
            if bus == -1:
                continue
            if x % bus == 0:
                targetBus = bus
                break
        if targetBus != -1:
            break
        x += 1
    print(targetBus * (x - depart))

def part2():
    values = []
    for i, bus in enumerate(buses):
        if bus != -1:
            values.append((bus, i))
    values = sorted(values)

    b = 1
    step = 1
    firstValue, firstValueOffset = values[-1]
    values = values[:-1]
    for p, c in values:
        for a in range(b, 100000000000000000000, step):
            x = firstValue * a - firstValueOffset + c
            if x % p == 0:
                b = a
                break
        step *= p
    x = firstValue * b - firstValueOffset
    print(x)

part1()
part2()
