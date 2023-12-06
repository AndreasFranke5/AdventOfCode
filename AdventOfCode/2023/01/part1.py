import os

def nums(path):
    total=0
    with open(path, 'r') as f:
        for row in f:
            digs=[char for char in row if char.isdigit()]
            if digs:
                num=int(digs[0]+digs[-1])
                total+=num
    return total
dir=os.path.dirname(os.path.abspath(__file__))
path=os.path.join(dir, 'input')
total=nums(path)
print("Sum:", total)
