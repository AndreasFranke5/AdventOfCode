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

def possible(games, rmax, gmax, bmax):
    pgames=[]
    for id,rnds in games.items():
        yes=True
        for rndamts in rnds:
            if rndamts['red']>rmax or rndamts['green']>gmax or rndamts['blue']>bmax:
                yes=False
                break
        if yes:
            pgames.append(id)
    return pgames

path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')
with open(path, "r") as file:
    data=file.read()

games=read(data)
pgames=possible(games, 12, 13, 14)
print(f"ID sum: {sum(pgames)}")