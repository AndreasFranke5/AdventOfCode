import os
import math

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

# Checking every seed is very slow, so the range is divided into smaller groups and every n-th seed is checked instead.
# Square root of the range length is used as the iteration step size, so many individual seeds can be skipped and still cover the whole range.
# Whenever a new lowest value is found, a targeted search around the step size range of that value is made, to see if there is an even lower value.
# Repeat until no new lowest value is found.
def allseeds(nums, maps):
    low=float('inf')
    total=len(nums)//2
    for i in range(0, len(nums), 2):
        start=nums[i]
        srange=nums[i+1]
        step=int(math.sqrt(srange)) or 1
        print(f"Range {i//2+1}/{total} - Step: {step} - Start: {start} - Length: {srange}") # Prints progress to make sure that the program isn't stuck.
        prevlow=float('inf')
        for seed in range(start, start+srange, step):
            pos=oneseed(seed, maps)
            if pos<prevlow:
                prevlow=pos
                for refseed in range(max(seed-step, start), seed):
                    refpos = oneseed(refseed, maps)
                    low=min(low, refpos)
                low=min(low, pos)
    return low
path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(path, 'r') as file:
    data = file.readlines()
maps = read(data)
seedrange = find(data)
low = allseeds(seedrange, maps)
print(f"Lowest location number: {low}")