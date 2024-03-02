import os
from itertools import cycle
from math import lcm

path=os.path.join(os.path.dirname(__file__), 'input.txt')
with open(path) as file:
    header,_,*l=file.read().splitlines()

navigation={}
for line in l:
    a,b=line.split(' = ')
    c,d=b[1:-1].split(', ')
    navigation[a]=c,d

tot=0
currentLoc='AAA'
for direction in cycle(header):
    if direction=='L':
        currentLoc=navigation[currentLoc][0]
    elif direction=='R':
        currentLoc=navigation[currentLoc][1]
    else:
        raise ValueError()
    tot+=1
    if currentLoc=='ZZZ':
        break

print(f"Steps required: {tot}")
