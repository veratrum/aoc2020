from aoc import aopen
import re
from collections import defaultdict
from copy import deepcopy

field = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
field4 = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.'))))
with aopen(17) as f:
    initialData = [[c for c in line] for line in f.read().split('\n')]
    for i, row in enumerate(initialData):
        for j, x in enumerate(row):
            field[0][i][j] = x
            field4[0][0][i][j] = x

def getBounds(data):
    minZ = minY = minX = 99999
    maxZ = maxY = maxX = -99999
    for z in list(data.keys()):
        plane = data[z]
        for y in list(plane.keys()):
            row = plane[y]
            for x in list(row.keys()):
                if row[x] == '.':
                    continue
                if x < minX:
                    minX = x
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
                if y > maxY:
                    maxY = y
                if z < minZ:
                    minZ = z
                if z > maxZ:
                    maxZ = z
    return minZ, maxZ, minY, maxY, minX, maxX

def getBounds4(data):
    minZ = minY = minX = minW = 99999
    maxZ = maxY = maxX = maxW = -99999
    for w in list(data.keys()):
        cube = data[w]
        for z in list(cube.keys()):
            plane = cube[z]
            for y in list(plane.keys()):
                row = plane[y]
                for x in list(row.keys()):
                    if row[x] == '.':
                        continue
                    if w < minW:
                        minW = w
                    if w > maxW:
                        maxW = x
                    if x < minX:
                        minX = x
                    if x > maxX:
                        maxX = x
                    if y < minY:
                        minY = y
                    if y > maxY:
                        maxY = y
                    if z < minZ:
                        minZ = z
                    if z > maxZ:
                        maxZ = z
    return minZ, maxZ, minY, maxY, minX, maxX, minW, maxW

def countNeighbours(data, z, y, x):
    total = 0
    for a in range(z - 1, z + 2):
        for b in range(y - 1, y + 2):
            for c in range(x - 1, x + 2):
                if a == z and b == y and c == x:
                    continue
                if data[a][b][c] == '#':
                    total += 1
    return total

def countNeighbours4(data, z, y, x, w):
    total = 0
    for d in range(w - 1, w + 2):
        for a in range(z - 1, z + 2):
            for b in range(y - 1, y + 2):
                for c in range(x - 1, x + 2):
                    if d == w and a == z and b == y and c == x:
                        continue
                    if data[d][a][b][c] == '#':
                        total += 1
    return total

def countActive(data):
    total = 0
    for plane in data.values():
        for row in plane.values():
            for x in row.values():
                if x == '#':
                    total += 1
    return total

def countActive4(data):
    total = 0
    for cube in data.values():
        for plane in cube.values():
            for row in plane.values():
                for x in row.values():
                    if x == '#':
                        total += 1
    return total

def tick(data):
    minZ, maxZ, minY, maxY, minX, maxX = getBounds(data)
    newData = deepcopy(data)
    for z in range(minZ - 1, maxZ + 2):
        plane = data[z]
        for y in range(minY - 1, maxY + 2):
            row = plane[y]
            for x in range(minX - 1, maxX + 2):
                value = row[x]
                count = countNeighbours(data, z, y, x)
                if value == '#':
                    if count < 2 or count > 3:
                        value = '.'
                else:
                    if count == 3:
                        value = '#'
                
                newData[z][y][x] = value
    return newData

def tick4(data):
    minZ, maxZ, minY, maxY, minX, maxX, minW, maxW = getBounds4(data)
    newData = deepcopy(data)
    for w in range(minW - 1, maxW + 2):
        cube = data[w]
        for z in range(minZ - 1, maxZ + 2):
            plane = cube[z]
            for y in range(minY - 1, maxY + 2):
                row = plane[y]
                for x in range(minX - 1, maxX + 2):
                    value = row[x]
                    count = countNeighbours4(data, z, y, x, w)
                    if value == '#':
                        if count < 2 or count > 3:
                            value = '.'
                    else:
                        if count == 3:
                            value = '#'
                    
                    newData[w][z][y][x] = value
    return newData

for i in range(6):
    field = tick(field)
    field4 = tick4(field4)

print(countActive(field))
print(countActive4(field4))