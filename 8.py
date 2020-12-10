from aoc import aopen
import re

with aopen(8) as f:
    p = re.compile(r'(\w+) ([+-])(\d+)')
    lines = []
    for line in f.readlines():
        m = p.match(line)
        lines.append((m.group(1), int(m.group(3)) * (-1 if m.group(2) == '-' else 1)))

instructions = {
    'acc': lambda ip, ac, x: (ip + 1, ac + x),
    'jmp': lambda ip, ac, x: (ip + x, ac),
    'nop': lambda ip, ac, x: (ip + 1, ac),
}

ip = 0
ac = 0
traversed = set()
while ip not in traversed:
    traversed.add(ip)
    line = lines[ip]
    ip, ac = instructions[line[0]](ip, ac, line[1])

print(ac)

for i in range(len(lines)):
    if lines[i][0] == 'acc':
        continue

    ip = 0
    ac = 0
    traversed = set()
    while ip not in traversed and ip < len(lines):
        traversed.add(ip)
        line = lines[ip]
        if ip == i:
            ip, ac = instructions['nop' if line[0] == 'jmp' else 'jmp'](ip, ac, line[1])
        else:
            ip, ac = instructions[line[0]](ip, ac, line[1])
    
    if ip >= len(lines):
        print(ac)
        break
