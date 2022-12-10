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

def move_tail(H,T,H_last_step):
    if(H[0]-T[0] == 0 or H[1]-T[1]==0):
        #X
        if H[0]-T[0] > 1:
            T[0] += 1
        elif -1 > H[0]-T[0]:
            T[0] -= 1
        #Y
        if H[1]-T[1] > 1:
            T[1] += 1
        elif -1 > H[1]-T[1]:
            T[1] -= 1
    elif H[0]-T[0] in (2,-2) or H[1]-T[1] in (2,-2):
        T=H_last_step

    return(T)

#def move_knot(H,T,H_last_step):
    

input = open("input_medium","r")
input_file = input.read().splitlines()
input.close()

#Answer1
H = [0,0]
T = [0,0]
unique_coordinates = []
for line in input_file:
    direction, steps = line.split(' ')
    for step in range(int(steps)):
        H_last_step = H.copy()
        H = move_head(direction,H)
        T = move_tail(H,T,H_last_step)
        if T not in unique_coordinates:
            unique_coordinates.append(T.copy())

print(len(unique_coordinates))

#Answer2 -- IN DEV
knots = []
for x in range(10):
    knots.append([0,0])
unique_coordinates = []
i = 0
for line in input_file:
    direction, steps = line.split(' ')
    prev = []
    for step in range(int(steps)):
        #print("step",step)
        first = True
        for knot in knots:
            last_step = knot.copy()
            #print("last_step",last_step)
            if first:
                knot = move_head(direction,knot)
                #print("first",knots)
                first = False
            else:
                #print("prev",prev)
                knot = move_tail(prev,knot,last_step)
                #print("tail",knots)
                if i == 9 and knot not in unique_coordinates:
                    unique_coordinates.append(knot.copy())
            #print(knot)
            prev = knot.copy()
            i += 1 # tired so using this for now
        #print("prev",prev)
    i = 0
    print("knots",knots)   
print(len(unique_coordinates))