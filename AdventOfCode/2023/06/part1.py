race=[(59,430), (70,1218), (78,1213), (78,1276)]

def wincombs(race):
    wincomb = []
    for time, record in race:
        comb = 0
        for buttonhold in range(time):
            speed=buttonhold
            traveltime=time-buttonhold
            dist=speed*traveltime
            if dist>record:
                comb+=1
        wincomb.append(comb)
    totalcomb = 1
    for comb in wincomb:
        totalcomb*=comb
    return totalcomb, wincomb

result=wincombs(race)
print(f"Total amount of ways to win: {result}")