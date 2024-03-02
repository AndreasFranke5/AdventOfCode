import os

def count(row):
    left, right=row.split("|")
    lottery_nums=left.split()
    my_nums=right.split()
    count=0
    for num in my_nums:
        for lottery_num in lottery_nums:
            if num==lottery_num:
                count += 1
                break
    return count

def read(path):
    with open(path, 'r') as file:
        ticket=[line.strip().split(':', 1)[1].strip() for line in file if line.strip()]
    ticket_dict={i:1 for i in range(len(ticket))}
    i=0
    while i<len(ticket):
        match=count(ticket[i])
        for j in range(1,match+1):
            if i+j<len(ticket):
                ticket_dict[i+j]+=ticket_dict[i]
        i+=1
    total=sum(ticket_dict.values())
    return total

path=os.path.join(os.path.dirname(__file__),'input.txt')
total = read(path)
print(f"Total amount: {total}")

