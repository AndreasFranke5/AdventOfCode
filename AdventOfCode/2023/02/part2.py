import os

def read(data):
    games={}
    for game in data.split("\n"):
        if not game.strip():
            continue
        id,totalrnds=game.split(":")
        id=int(id.split()[1])
        rnds=totalrnds.split(";")
        rndsamt=[]
        for rnd in rnds:
            colors=rnd.strip().split(",")
            rndamt={'red': 0, 'green': 0, 'blue': 0}
            for color in colors:
                amt,cname=color.strip().split()
                rndamt[cname]=int(amt)
            rndsamt.append(rndamt)
        games[id]=rndsamt
    return games

def minimum_cubes(games):
    min_cubes={}
    for id,rnds in games.items():
        minset = {'red': 0, 'green': 0, 'blue': 0}
        for rndamt in rnds:
            minset['red']=max(minset['red'], rndamt.get('red', 0))
            minset['green']=max(minset['green'], rndamt.get('green', 0))
            minset['blue']=max(minset['blue'], rndamt.get('blue', 0))
        min_cubes[id]=minset
    return min_cubes

def powercalc(min_cubes):
    tot=0
    for id,cubes in min_cubes.items():
        p=cubes['red']*cubes['green']*cubes['blue']
        tot+=p
    return tot

path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')
with open(path, "r") as file:
    data = file.read()

games=read(data)
mins=minimum_cubes(games)
tot = powercalc(mins)
print(f"Total power: {tot}")