import os

def read(data):
    maps = {}
    cmap = ""
    for line in data:
        if ':' in line:
            cmap = line.split(':')[0]
            maps[cmap]=[]
        elif line.strip():
            parts=[int(n) for n in line.split()]
            maps[cmap].append(parts)
    return maps

def find(data):
    for line in data:
        if line.startswith('seeds:'):
            nums=[int(n) for n in line.split()[1:]]
            return nums

def mapping(num, maplist):
    for m in maplist:
        dest, source, srange = m
        if source<=num<source+srange:
            return dest+(num-source)
    return num

def oneseed(seed, maps):
    cval=seed
    for mapname in maps:
        cval = mapping(cval, maps[mapname])
    return cval

path=os.path.join(os.path.dirname(__file__),'input.txt')
with open(path, 'r') as file:
    data = file.readlines()
maps = read(data)
nums = find(data)
pos=[oneseed(num, maps) for num in nums]
low = min(pos)
print(f"Lowest location number: {low}")
