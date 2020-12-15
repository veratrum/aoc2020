from aoc import aopen

with aopen(15) as f:
    numbers = [int(x) for x in f.read().split(',')]

def findValue(limit):
    sequence = numbers.copy()
    last1 = {k: i + 1 for i, k in enumerate(sequence)}
    last2 = {k: None for k in sequence}

    i = len(sequence) + 1
    last = sequence[-1]
    while i <= limit:
        if last2[last] is None:
            x = 0
        else:
            x = last1[last] - last2[last]

        if x in last1:
            last2[x] = last1[x]
        else:
            last2[x] = None
        last1[x] = i
        last = x
        i += 1
    print(x)

findValue(2020)
findValue(30000000)