import os

# Created a 140 x 140 grid for the input file, then checked each cell at row and col +/-1 for adjacency.
# Similar to part 1, but modified to look for the "*" symbol and check for adjacent numbers.

def read(data):
    with open(path,'r') as file:
        data=file.read()
    grid=[list(row) for row in data.splitlines()]
    nums=[]
    symbol=[]
    for i,row in enumerate(grid):
        num=''
        for j,char in enumerate(row):
            if char.isdigit():
                num+=char
            else:
                if num:
                    nums.append({'val':num,'firstpos':(i,j-len(num)),'lastpos':(i,j-1)})
                    num=''
                if char!='.':
                    symbol.append({'val':char,'pos':(i,j)})
        if num:
            nums.append({'val':num,'firstpos':(i,j+1-len(num)),'lastpos':(i,j)})
    return nums,symbol

def adjacency(num,s):
    numfirst,numlast=num['firstpos'],num['lastpos']
    symbolpos=s['pos']
    return (numfirst[0]-1<=symbolpos[0]<=numlast[0]+1) and (numfirst[1]-1<=symbolpos[1]<=numlast[1]+1)

def result(data):
    nums,symbol=read(data)
    total=0
    for s in symbol:
        if s['val']=='*':
            adjacent=[num for num in nums if adjacency(num,s)]
            if len(adjacent)==2:
                total+=int(adjacent[0]['val'])*int(adjacent[1]['val'])
    return total

path=os.path.join(os.path.dirname(__file__),'input')
print(f"Sum: {result(path)}")