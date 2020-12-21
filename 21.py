from aoc import aopen
from collections import defaultdict
import re

lines = []
with aopen(21) as f:
    strings = f.readlines()
    for line in strings:
        m = re.match(r'(.*) \(contains (.*)\)', line)
        lines.append([m.group(1).split(' '), m.group(2).split(', ')])

def findPotentialAllergens(lines):
    allergensReverse = defaultdict(list)
    for line in lines:
        ingredients, allergens = line
        for allergen in allergens:
            allergensReverse[allergen].append(list(ingredients))
    
    potentialAllergens = set()
    for allergen, ingredients in allergensReverse.items():
        for ingredientList in ingredients:
            for i in ingredientList:
                valid = True
                for testIngredientList in ingredients:
                    if not i in testIngredientList:
                        valid = False
                if valid:
                    potentialAllergens.add(i)

    return potentialAllergens

def findAllergens(lines):
    allergensReverse = defaultdict(list)
    for line in lines:
        ingredients, allergens = line
        for allergen in allergens:
            allergensReverse[allergen].append(list(ingredients))
    
    confirmedAllergens = defaultdict(set)
    for allergen, ingredients in allergensReverse.items():
        for ingredientList in ingredients:
            for i in ingredientList:
                valid = True
                for testIngredientList in ingredients:
                    if not i in testIngredientList:
                        valid = False
                if valid and i not in confirmedAllergens[allergen]:
                    confirmedAllergens[allergen].add(i)

    finalAllergens = {}
    for _ in range(len(confirmedAllergens.keys())):
        for k, v in confirmedAllergens.items():
            if k in finalAllergens.keys():
                continue
            v = [x for x in v if x not in finalAllergens.values()]
            if len(v) == 1:
                finalAllergens[k] = v[0]
                break

    return finalAllergens

def part1():
    potentialAllergens = findPotentialAllergens(lines)
    total = 0
    for line in lines:
        for i in line[0]:
            if i not in potentialAllergens:
                total += 1
    print(total)

def part2():
    allergens = findAllergens(lines)
    print(','.join([allergens[k] for k in sorted(allergens.keys())]))

part1()
part2()
