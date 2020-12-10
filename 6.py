from aoc import aopen
import re

with aopen(6) as f:
    groups = [x.split('\n') for x in f.read().split('\n\n')]

total = 0
for group in groups:
    answered = set()
    count = 0
    for person in group:
        for letter in person:
            if letter not in answered:
                answered.add(letter)
                count += 1
    total += count

print(total)


total = 0
for group in groups:
    answered = set(group[0])
    for person in group[1:]:
        for letter in set(answered):
            if letter not in person:
                answered.remove(letter)
    total += len(answered)

print(total)