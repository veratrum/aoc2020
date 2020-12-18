from aoc import aopen
import re

with aopen(18) as f:
    lines = f.readlines()
    lines = [line.replace(' ', '').replace('\n', '') for line in lines]

def findCloseBracket(line):
    opens = 0
    for i, c in enumerate(line):
        if c == '(':
            opens += 1
        elif c == ')':
            opens -= 1
            if opens == 0:
                return i

def process(line):
    i = 0
    result = -1
    while i < len(line):
        c = line[i]
        value = None
        if c == '(':
            j = i + findCloseBracket(line[i:])
            value = process(line[i+1:j])
            line = line[:i] + line[j+1:]
        elif c in '1234567890':
            value = int(c)
        if value is not None:
            if result == -1:
                result = value
            elif line[i-1] == '+':
                result += value
            elif line[i-1] == '*':
                result *= value
        i += 1
    return result

def findNumber(line):
    l = 0
    n = 0
    while l < len(line) and line[l] in '1234567890':
        n *= 10
        n += int(line[l])
        l += 1
    return n, l

def process2(line):
    i = 0
    done = False
    while not done:
        i = 0
        while i < len(line):
            c = line[i]
            if c == '(':
                j = i + findCloseBracket(line[i:])
                value = process2(line[i+1:j])
                line = line[:i] + str(value) + line[j+1:]
                i = 0
                continue
            n, l = findNumber(line[i:])
            if n != 0:
                if i+l < len(line) and line[i+l] == '+':
                    n2, l2 = findNumber(line[i+l+1:])
                    if n2 != 0:
                        line = line[:i] + str(n + n2) + line[i+l+l2+1:]
                        i = 0
                        continue
            i += 1
        i = 0
        while i < len(line):
            c = line[i]
            if c == '(':
                j = i + findCloseBracket(line[i:])
                value = process2(line[i+1:j])
                line = line[:i] + str(value) + line[j+1:]
                i = 0
                continue
            n, l = findNumber(line[i:])
            if n != 0:
                if i+l < len(line) and line[i+l] == '*':
                    n2, l2 = findNumber(line[i+l+1:])
                    if n2 != 0:
                        line = line[:i] + str(n * n2) + line[i+l+l2+1:]
                        i = 0
                        continue
            i += 1
        
        n, l = findNumber(line)
        if len(line) == l:
            return int(line)

total = 0
total2 = 0
for line in lines:
    total += process(line)
    total2 += process2(line)
print(total)
print(total2)