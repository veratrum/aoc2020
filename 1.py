from aoc import aopen

with aopen(1) as f:
    values = [int(x) for x in f.readlines()]

valuesReverse = set()
for value in values:
    valuesReverse.add(value)

for value in values:
    if 2020 - value in valuesReverse:
        print(value * (2020 - value))

for i, value in enumerate(values):
    for value2 in values[i+1:]:
        if 2020 - value - value2 in valuesReverse:
            print(value * value2 * (2020 - value - value2))
