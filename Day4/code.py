def get_elf_sections(line):
    elf1,elf2 = line.split(',')
    elf1_low,elf1_high=elf1.split('-')
    elf1_sections = list(range(int(elf1_low),int(elf1_high)+1))
    elf2_low,elf2_high=elf2.split('-')
    elf2_sections = list(range(int(elf2_low),int(elf2_high)+1))

    return elf1_sections, elf2_sections

input = open("input","r")
input_file = input.read().splitlines()
input.close()

count_overlaps = 0
for line in input_file:
    elf1_sections, elf2_sections = get_elf_sections(line)

    if set(elf1_sections).issubset(elf2_sections):
        count_overlaps += 1
    elif set(elf2_sections).issubset(elf1_sections):
        count_overlaps += 1

print(count_overlaps) #Answer1

count_overlaps = 0
for line in input_file:
    elf1_sections, elf2_sections = get_elf_sections(line)

    for section in elf1_sections:
        if section in elf2_sections:
            count_overlaps+=1
            break

print(count_overlaps) #Answer2