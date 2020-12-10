from aoc import aopen
import re

with aopen(2) as f:
    strings = list(f.readlines())

total = 0
for s in strings:
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', s)
    a = int(m.group(1))
    b = int(m.group(2))
    letter = m.group(3)
    code = m.group(4)
    c = code.count(letter)
    if a <= c <= b:
        total += 1

print(total)

total = 0
for s in strings:
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', s)
    a = int(m.group(1))
    b = int(m.group(2))
    letter = m.group(3)
    code = m.group(4)
    found = 0
    for i in [a, b]:
        if code[i - 1] == letter:
            found += 1
            if found == 2:
                break
    if found == 1:
        total += 1

print(total)
