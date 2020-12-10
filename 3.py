from aoc import aopen

with aopen(3) as f:
    trees = [[c == '#' for c in x] for x in f.readlines()]

y = 0
total = 0
for x in range(len(trees)):
    if trees[x][y]:
        total += 1
    y += 3
    y %= 31

print(total)

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
)
result = 1
for slope in slopes:
    y = 0
    total = 0
    for x in range(0, len(trees), slope[1]):
        if trees[x][y]:
            total += 1
        y += slope[0]
        y %= 31
    result *= total
print(result)