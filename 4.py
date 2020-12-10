from aoc import aopen
import re

with aopen(4) as f:
    passports = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
total = 0
for passport in passports:
    found = 0
    for field in fields:
        if field + ':' in passport:
            found += 1
    if found == 7:
        total += 1

print(total)

total = 0
for passport in passports:
    found = 0
    valid = True
    for field in fields:
        s = re.search(field + ':(\S+)', passport)
        if not s:
            valid = False
            continue
        x = s.group(1)
        if field in ('byr', 'iyr', 'eyr', 'pid') and not re.match(r'[0-9]+', x):
            valid = False
        if field == 'byr' and not 1920 <= int(x) <= 2002:
            valid = False
        elif field == 'iyr' and not 2010 <= int(x) <= 2020:
            valid = False
        elif field == 'eyr' and not 2020 <= int(x) <= 2030:
            valid = False
        elif field == 'hgt':
            m1 = re.match(r'(\d+)cm$', x)
            m2 = re.match(r'(\d+)in$', x)
            if m1:
                if not re.match(r'[0-9]+', m1.group(1)) or not 150 <= int(m1.group(1)) <= 193:
                    valid = False
            elif m2:
                if not re.match(r'[0-9]+', m2.group(1)) or not 59 <= int(m2.group(1)) <= 76:
                    valid = False
            else:
                valid = False
        elif field == 'hcl' and not re.match(r'#[0-9a-f]{6}$', x):
            valid = False
        elif field == 'ecl' and x not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False
        elif field == 'pid' and not len(x) == 9:
            valid = False
    if valid:
        total += 1

print(total)
