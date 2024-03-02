import os

dictionary = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

# Iterates over each row in the input file. Uses two indices, 'i' and 'j'. 
# 'i' will increment until it finds a character, then 'j' will decrement, until
# the elements between 'i' and 'j' correspond to a word in the dictionary.
# If it doesn't correspond, 'i' increments. May not be efficient but does the trick.
def letters_to_nums(s):
    new_value = []
    i=0
    while i<len(s):
        if s[i].isdigit():
            new_value.append(s[i])
            i+=1
        else:
            j=i
            while j>=0:
                substring=s[j:i+1]
                if substring in dictionary:
                    new_value.append(dictionary[substring])
                    break
                j-=1
            i+=1
    return ''.join(new_value)

def check_file(file_name):
    values = []
    complete_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(complete_path, 'r') as file:
        for line in file:
            checked_row=letters_to_nums(line.strip())
            if checked_row:
                if len(checked_row)==1:
                    checked_row*=2
                first_num=checked_row[0]
                last_num=checked_row[-1]
                new_num=int(first_num+last_num)
                values.append(new_num)
    return values

file_name = 'input.txt'
new_values = check_file(file_name)
print("Sum:", sum(new_values))