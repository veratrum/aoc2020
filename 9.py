
with open('input\\9.txt', 'r') as f:
    values = [int(x) for x in f.readlines()]

n = 25

for i, x in enumerate(values[n:]):
    previous = values[i:i+n]

    valid = False
    for p in previous:
        if p * 2 != x and x - p in previous:
            valid = True
            break
    
    if not valid:
        secret = x
        print(secret)
        break


for i, x in enumerate(values):
    total = x
    found = [x]
    for j, y in enumerate(values[i+1:]):
        total += y
        found.append(y)
        if total == secret:
            print(min(found) + max(found))
            break
        elif total > secret:
            break