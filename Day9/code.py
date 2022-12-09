#IN DEVELOPMENT

def move_head(direction,H):
    if direction == 'R':
        H[0] += 1
    elif direction == 'L':
        H[0] += -1
    elif direction == 'U':
        H[1] += 1
    elif direction == 'D':
        H[1] += -1
    return H

def move_tail(H,T):
    if H[0]-T[0] > 1:
        T[0] += 1
    elif -1 < H[0]-T[0] > 1:
        T[0] -= 1
    return(T)

input = open("input_small","r")
input_file = input.read().splitlines()
input.close()

H = [0,0]
T = [0,0]

for line in input_file:
    direction, steps = line.split(' ')
    for step in range(int(steps)):
        H = move_head(direction,H)
        print("H",H)
        T = move_tail(H,T)
        print("T",T)
