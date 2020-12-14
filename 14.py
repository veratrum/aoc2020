from aoc import aopen
import re

with aopen(14) as f:
    lines = f.readlines()

def part1():
    variables = {}
    for i, line in enumerate(lines):
        if 'mask' in line:
            mask = line.partition(' = ')[2][:-1][::-1]
        else:
            m = re.match(r'mem\[(\d+)\] = (\d+)\n', line)
            v = int(m.group(1))
            x = '{:b}'.format(int(m.group(2)))[::-1].ljust(36, '0')
            
            result = 0
            p = 1
            for c1, c2 in zip(x, mask):
                if c2 == 'X':
                    result += p * int(c1)
                else:
                    result += p * int(c2)
                p *= 2
            variables[v] = result

    print(sum(variables.values()))

def part2():
    values = []
    for i, line in enumerate(lines):
        if 'mask' in line:
            mask = line.partition(' = ')[2][:-1][::-1]
        else:
            m = re.match(r'mem\[(\d+)\] = (\d+)\n', line)
            v = '{:b}'.format(int(m.group(1)))[::-1].ljust(36, '0')
            x = int(m.group(2))
            
            addresses = [0]
            p = 1
            for c1, c2 in zip(v, mask):
                if c2 == 'X':
                    addresses += [a + p for a in addresses]
                else:
                    bit = 1 if c1 == '1' or c2 == '1' else 0
                    addresses = [a + bit * p for a in addresses]
                p *= 2
            
            for value, existingAddresses in values:
                toDelete = []
                for j, a in enumerate(existingAddresses):
                    if a in addresses:
                        toDelete.append(j)
                for j in toDelete[::-1]:
                    del existingAddresses[j]

            values.append((x, addresses))
        
    total = 0
    for value, existingAddresses in values:
        total += value * len(existingAddresses)
    print(total)

part1()
part2()