from aoc import aopen

with aopen(12) as f:
    moves = f.readlines()

directionKeys = ['N', 'S', 'E', 'W']
directionValues = {'N': 0, 'S': 180, 'E': 90, 'W': 270}
rotationKeys = ['L', 'R']
rotationValues = {'L': -1, 'R': 1}

def doMove(position, direction, value):
    if direction == 0:
        position[1] += value
    elif direction == 90:
        position[0] += value
    elif direction == 180:
        position[1] -= value
    if direction == 270:
        position[0] -= value

def sailShip():
    direction = 90
    position = [0, 0]
    for move in moves:
        action = move[0]
        value = int(move[1:])

        if action in directionKeys:
            moveDirection = directionValues[action]
            doMove(position, moveDirection, value)
        elif action in rotationKeys:
            direction += rotationValues[action] * value
            direction %= 360
        elif action == 'F':
            doMove(position, direction, value)
        
    print(abs(position[0]) + abs(position[1]))

def rotateWaypoint(position, direction):
    newPosition = [0, 0]
    for _ in range(90, direction + 1, 90):
        newPosition[0] = position[1]
        newPosition[1] = -position[0]
        position[0] = newPosition[0]
        position[1] = newPosition[1]

def moveToWaypoint(shipPosition, waypointPosition, value):
    shipPosition[0] += waypointPosition[0] * value
    shipPosition[1] += waypointPosition[1] * value

def sailWaypoint():
    shipPosition = [0, 0]
    waypointPosition = [10, 1]
    for move in moves:
        action = move[0]
        value = int(move[1:])

        if action in directionKeys:
            moveDirection = directionValues[action]
            doMove(waypointPosition, moveDirection, value)
        elif action in rotationKeys:
            rotateWaypoint(waypointPosition, (rotationValues[action] * value) % 360)
        elif action == 'F':
            moveToWaypoint(shipPosition, waypointPosition, value)
    
    print(abs(shipPosition[0]) + abs(shipPosition[1]))

sailShip()
sailWaypoint()
