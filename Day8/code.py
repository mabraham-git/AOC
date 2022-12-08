import numpy as np

def check_view(list, val):  
    number_of_trees_seen = 0
    if len(list)==0:
        return 0

    for x in list: 
        number_of_trees_seen += 1
        if val <= x:
            break

    return number_of_trees_seen

def check_visibility(list, val):  
    visible = True
    for x in list:
        if val <= x:
            visible = False
    return visible

def check_tree_view(row,column,matrix):
    #trees left choosen tree
    left = check_view(np.flip(matrix[row,:column]),matrix[row][column])
    #trees right choosen tree
    right = check_view(matrix[row,column+1:],matrix[row][column])
    #trees top choosen tree
    top = check_view(np.flip(matrix[:row,column]),matrix[row][column])
    #trees below choosen tree
    below = check_view(matrix[row+1:,column],matrix[row][column])

    return([left,right,top,below])

def check_tree_visibility(row,column,matrix):

    #trees left choosen tree
    left = check_visibility(matrix[row,:column],matrix[row][column])
    #trees right choosen tree
    right = check_visibility(matrix[row,column+1:],matrix[row][column])
    #trees top choosen tree
    top = check_visibility(matrix[:row,column],matrix[row][column])
    #trees below choosen tree
    below = check_visibility(matrix[row+1:,column],matrix[row][column])

    return [left,right,top,below]

input = open("input","r")
input_file = input.read().splitlines()
input.close()

trees = []

for line in input_file:
    trees.append(list(line))

np_trees = np.array(trees)

#Answer 1
sum = 0
for idx, x in np.ndenumerate(np_trees):
    if(any(check_tree_visibility(idx[0],idx[1], np_trees))):
        sum += 1
print(sum)

#Answer 2
highest_score = 0
for idx, x in np.ndenumerate(np_trees):
    left,right,top,below = check_tree_view(idx[0],idx[1], np_trees)
    if left*right*top*below > highest_score:
        highest_score = left*right*top*below
print(highest_score)