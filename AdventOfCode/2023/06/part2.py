race=[(59707878,430121812131276)]

def wincombs(race):
    time,record=race[0]
    comb = 0
    for buttonhold in range(time):
        speed=buttonhold
        traveltime=time-buttonhold
        dist=speed*traveltime
        if dist>record:
            comb+=1
    return comb
result=wincombs(race)
print(f"Total amount of ways to win: {result}")