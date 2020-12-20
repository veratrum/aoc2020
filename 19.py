from aoc import aopen
import re

rules = {}
with aopen(19) as f:
    rulesLines, lines = [x.split('\n') for x in f.read().split('\n\n')]

    for rule in rulesLines:
        if '"' in rule:
            m = re.match(r'(\d+): \"(\w)\"', rule)
            i = int(m.group(1))
            rules[i] = m.group(2)
        else:
            m = re.match(r'(\d+): ', rule)
            i = int(m.group(1))
            rest = rule[m.end(1) + 2:]
            rest = rest.split('|')
            rest = [[int(y) for y in x.split(' ') if y not in ['', ' ']] for x in rest]
            rules[i] = rest

def checkRule(i, s):
    rule = rules[i]
    if len(s) == 0:
        return False, ''
    if isinstance(rule, str):
        return rule == s[0], s[1:]

    valid = False
    for conditionalRule in rule:
        _s = s
        _valid = True
        for ruleID in conditionalRule:
            __valid, _s = checkRule(ruleID, _s)
            if not __valid:
                _valid = False
                break
        if _valid:
            return True, _s

    return False, ''

def checkRuleLoop(i, s, n8, n11):
    rule = rules[i]
    if len(s) == 0:
        return False, ''
    if isinstance(rule, str):
        return rule == s[0], s[1:]

    valid = False
    lastValid = None
    for conditionalRule in rule:
        _s = s
        _valid = True
        for ruleID in conditionalRule:
            if ruleID == 8:
                ruleID *= 10 ** n8
            elif ruleID == 11:
                ruleID *= 10 ** n11
            __valid, _s = checkRuleLoop(ruleID, _s, n8, n11)
            if not __valid:
                _valid = False
                break
        if _valid:
            lastValid = [True, _s]

    if lastValid:
        return lastValid
    return False, ''

def part1():
    total = 0
    for line in lines:
        valid, s = checkRule(0, line)
        if valid and len(s) == 0:
            total += 1
    print(total)

def part2():
    for i in range(2, 20):
        rules[8 * 10 ** i] = [[42] * (i - 1)]
        rules[11 * 10 ** i] = [[42] * (i - 1) + [31] * (i - 1)]

    total = 0
    for line in lines:
        valid = False
        for i in range(2, 20):
            for j in range(2, 20):
                _valid, s = checkRuleLoop(0, line, i, j)
                if _valid and len(s) == 0:
                    valid = True
                    total += 1
                    break
            if valid:
                break
    print(total)

part1()
part2()