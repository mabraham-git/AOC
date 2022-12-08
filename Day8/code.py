# IN DEVELOPMENT!

import numpy as np

input = open("input_small","r")
input_file = input.read().splitlines()
input.close()

trees = []

for line in input_file:
    trees.append(list(line))

test = np.array(trees)

print(test)

rad = 2
column = 4



rad-=1
column-=1
#[row][element]
print("The tree:",test[rad][column])
print("trees after:",test[rad,column+1:])
print("trees before:",test[rad,:column])

print("trees under:",test[rad+1:,column])
print("trees over:",test[:rad,column])