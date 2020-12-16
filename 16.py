from aoc import aopen
import re
from collections import defaultdict

with aopen(16) as f:
    constraintStrings, yourTicket, tickets = f.read().split('\n\n')

    constraints = []
    for constraint in constraintStrings.split('\n'):
        m = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', constraint)
        constraints.append([m.group(1)] + [int(m.group(i)) for i in range(2, 6)])

    yourTicket = [int(x) for x in yourTicket.split('\n')[1].split(',')]
    tickets = [[int(x) for x in ticket.split(',')] for ticket in tickets.split('\n')[1:]]

def isValidForAny(value):
    for c in constraints:
        if isValidFor(value, c):
            return True
    return False

def isValidFor(value, c):
    return c[1] <= value <= c[2] or c[3] <= value <= c[4]

total = 0
validTickets = []
for ticket in tickets:
    valid = True
    for x in ticket:
        if not isValidForAny(x):
            valid = False
            total += x
    if valid:
        validTickets.append(ticket)

print(total)

found = []
foundValues = {}
while len(constraints) > 0:
    isNot = defaultdict(list)
    for ticket in validTickets:
        couldBe = defaultdict(list)
        for i in range(20):
            if i in found:
                continue
            for c in constraints:
                x = ticket[i]
                if isValidFor(x, c) and i not in couldBe[c[0]]:
                    couldBe[c[0]].append(i)
        for c, l in couldBe.items():
            if len(l) != 20:
                for i in range(20):
                    if i not in l and i not in isNot[c]:
                        isNot[c].append(i)
    for c, l in isNot.items():
        if len(l) == 19:
            right = -1
            for i in range(20):
                if i not in l:
                    right = i
            found.append(right)
            foundValues[c] = right
            constraints = [x for x in constraints if x[0] != c]

result = 1
for c, i in foundValues.items():
    if 'departure' in c:
        result *= yourTicket[i]
print(result)
