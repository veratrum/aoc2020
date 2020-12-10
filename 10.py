from aoc import aopen
from functools import cache

with aopen(10) as f:
    values = sorted([int(x) for x in f.readlines()])

x = 0
ones = 0
threes = 1
for value in values:
    delta = value - x
    if delta == 1:
        ones += 1
    elif delta == 3:
        threes += 1
    x = value
values = [0] + values

print(ones * threes)

@cache
def f(i):
    if i == len(values) - 1:
        return 1

    result = 0
    for j in range(i + 1, i + 4):
        if j >= len(values):
            break
        elif values[j] - values[i] <= 3:
            result += f(j)
        else:
            break
    return result

print(f(0))
