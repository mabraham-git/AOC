import numpy as np

def move_box(box_list,fromx,to,amount,cranemaster):
    if cranemaster == 9000:
        for i in range(amount):
            box_list[to-1].append(box_list[fromx-1][-1])
            box_list[fromx-1].pop()
        return box_list
    elif cranemaster == 9001:
        box_list[to-1].extend(box_list[fromx-1][-amount:])
        for i in range(amount):
            box_list[fromx-1].pop()
        return box_list

#amount, from, to
def extract_movement(command):
    command = command.split(" ")
    return command[command.index("move")+1],command[command.index("from")+1],command[command.index("to")+1]

def prepare_input(input_file):
    columns_idx = dict([]) #mapping
    box_columns = []
    start_commands_row = 0
    for line in input_file:
        start_commands_row += 1
        if line == "":
            break
        image_row = []
        for char in line:
            image_row.append(char)
        box_columns.append(image_row)

    for idx, char in enumerate(input_file[start_commands_row-2]):
        if char != " ":
            columns_idx[char]=idx

    box_lists = []

    box_columns.pop()
    numpy_box_column = np.array(box_columns)

    for a in columns_idx:
        box_lists.append(numpy_box_column[:,columns_idx[a]].tolist())

    for list in box_lists: 
        list = list.reverse()

    for boxes in box_lists:
        while " " in boxes:
            boxes.remove(" ")
    return box_lists, start_commands_row

def run_commands(input_file, start_commands_row, box_lists, cranemaster):
    for command in input_file[start_commands_row:]:
        amount, from_, to = extract_movement(command)
        move_box(box_lists, int(from_), int(to), int(amount),cranemaster)
    return(prepare_output(box_lists))

def prepare_output(box_lists):
    output = ""
    for list in box_lists:
        output+=list[-1]
    return(output)

def run(input_file, cranemaster):
    box_lists, start_commands_row = prepare_input(input_file)
    return run_commands(input_file, start_commands_row, box_lists, cranemaster)


input = open("input.txt","r")
input_file = input.read().splitlines()
input.close()

#creanemaster
print(run(input_file, 9000))
print(run(input_file, 9001))