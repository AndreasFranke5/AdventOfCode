import os

def calc_points(row):
    left, right=row.split("|")
    lottery_nums=left.split()
    my_nums=right.split()
    points=0
    first_win=True

    for num in my_nums:
        for lottery_num in lottery_nums:
            if num==lottery_num:
                if first_win:
                    points=1
                    first_win=False
                else:
                    points *= 2
                break
    return points

def read(path):
    total=0
    with open(path,'r') as file:
        for line in file:
            line=line.strip()
            if line:
                _, after_colon=line.split(':', 1)
                points=calc_points(after_colon.strip())
                total+=points
    return total

path=os.path.join(os.path.dirname(__file__),'input.txt')
result=read(path)
print(f"Points: {result}")