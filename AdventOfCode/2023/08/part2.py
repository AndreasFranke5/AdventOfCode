import os
from itertools import cycle
from functools import reduce
from math import lcm

path=os.path.join(os.path.dirname(__file__), 'input')
with open(path) as file:
    header,_,*l=file.read().splitlines()

navigation={}
newGhost=[]
for line in l:
    a,b=line.split(' = ')
    c,d=b[1:-1].split(', ')
    navigation[a]=c,d
    if a[-1]=='A':
        newGhost.append(a)

tot=0
for i, currentLoc in enumerate(newGhost):
    ghostID=0
    for direction in cycle(header):
        if direction=='L':
            currentLoc=navigation[currentLoc][0]
        elif direction=='R':
            currentLoc=navigation[currentLoc][1]
        else:
            raise ValueError()
        ghostID+=1
        if currentLoc.endswith('Z'):
            newGhost[i]=ghostID
            print(f"{ghostID} (Ghost {i+1})")
            break

tot=reduce(lcm,newGhost,1)
print(f"Steps required: {tot}")
