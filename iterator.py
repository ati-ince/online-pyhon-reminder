
# data = {'jn','al','at','xi'} # set

# Data = {el.upper() for el in data}

# print(type(Data), Data)

## generator use with iterator as an examole 

# lets say file name is hashtable.txt

# import sys

# file_name = 'hashtable.txt'

# with open(file_name) as file:
#     hashtable = (h for h in file)

#     for line in hashtable:
#         if '1ecdb18ed254dcdf98477f63aa92af80' in line:
#             print('YESSS', line)

## random text creation and generaytor teest

from random_string import random_str

for _ in range(5):
    print(random_str(len_=100))