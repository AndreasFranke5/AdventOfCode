import os

# Creates a difference table where each new row will be populated with the differences of the previous row.
# Stops when a row only contains one value, since each new row will contain one value less than the previous row.
def createDiffTable(seq):
    diffTable=[]
    currentRow=seq
    diffTable.append(currentRow) 
    while len(currentRow)>1:
        nextRow=[]
        for i in range(len(currentRow)-1):
            diff=currentRow[i+1]-currentRow[i]
            nextRow.append(diff)
        diffTable.append(nextRow)
        currentRow=nextRow
    return diffTable

# Sums the last value of each row in the difference table to find the next extrapolated value of the original sequence.
def sumLastVal(table):
    epVal=table[0][-1] # epVal = extrapolated value
    for row in table[1:]:
        epVal+=row[-1]
    return epVal

def read(path):
    total=0
    with open(path, 'r') as file:
        for line in file:
            seq=list(map(int, line.split()))
 #           seq.reverse() # Activate this line for part 2
            table=createDiffTable(seq)
            nextVal=sumLastVal(table)
            total+=nextVal
    return total

path=os.path.join(os.path.dirname(__file__),'input')
total=read(path)
print("Sum of extrapolated values:", total)