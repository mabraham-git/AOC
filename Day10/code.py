import numpy as np
np.set_printoptions(edgeitems=30, linewidth=1000)


input = open("input","r")
input_file = input.read().splitlines()
input.close()

find_in = [20, 60, 100, 140, 180, 220]
CRT_rows = [40, 80, 120, 160, 200, 240]
cycle = 0
max_cycles = 240
line = 0
X = 1
addx_timer = 0
sum_of__signal_strengths = 0
CRT = []
current_crt_row = []
#loop
while cycle < max(find_in+CRT_rows):
    cycle += 1
    if line <= len(input_file)-1:
        current_command = input_file[line]
    else:
        current_command = "none"




    if (current_command == "noop"):
        line += 1
    if (current_command[:4] == "addx"):
        if addx_timer == 2:
            X += int(current_command[5:])
            addx_timer = 0
            line += 1
        addx_timer += 1

    if cycle in find_in:
        sum_of__signal_strengths = sum_of__signal_strengths + (X*cycle)

    if cycle%40 in [X,X+1,X+2]:
        current_crt_row.append('#')
    else:
        current_crt_row.append('.')
    if cycle in CRT_rows:
        CRT.append(current_crt_row)
        current_crt_row = []


print(sum_of__signal_strengths)
print(np.array(CRT))
