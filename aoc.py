import os

def aopen(day):
    return open(os.path.join('input', f'{day}.txt'), 'r')
