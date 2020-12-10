from aoc import aopen
import re

with aopen(7) as f:
    lines = f.readlines()

bags = []
bagsDict = {}
for line in lines:
    name = re.search(r'^(.*) bags contain', line).group(1)
    remainder = line.partition('contain ')[2].strip('.\n')
    if remainder == 'no other bags':
        inside = []
    else:
        inside = [(int(re.search(r'^(\d+) (.*) bags?$', segment).group(1)), re.search(r'^(\d+) (.*) bags?$', segment).group(2)) for segment in remainder.split(', ')]
    bags.append((name, inside))
    bagsDict[name] = inside

found = set(['shiny gold'])
oldFound = set()
while found != oldFound:
    oldFound = set(found)
    for bag, inside in bags:
        insideBags = set(x[1] for x in inside)
        if bag in found:
            continue
        if not insideBags.isdisjoint(found):
            found.add(bag)

print(len(found) - 1)

def countBags(name):
    inside = bagsDict[name]
    total = 1
    for count, insideName in inside:
        total += countBags(insideName) * count
    print(f'{name}: {total}')
    return total

print(countBags('shiny gold') - 1)
