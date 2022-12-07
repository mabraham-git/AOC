import string

input = open("D:\\Code\AOC\Day3\input.txt","r")
rucksack_list = input.read().splitlines()
input.close()

priority = dict(zip(list(string.ascii_lowercase)+list(string.ascii_uppercase),list(range(1, 53))))
rucksack_list_itemerror = []

for rucksack in rucksack_list:
    intemsincompartments = int(len(rucksack)/2)
    compartment1 = rucksack[:intemsincompartments]
    compartment2 = rucksack[intemsincompartments:len(rucksack)]

    for item in compartment1:
        if item in compartment2:
            rucksack_list_itemerror.append([rucksack,item,priority[item]])
            break

sum = 0
for itemerror in rucksack_list_itemerror:
    sum = sum+itemerror[2]

print(sum)

sum2 = 0
i=0
counter = 1
for rucksack in rucksack_list:
    if counter == 1:
        for item in rucksack:
            if item in rucksack_list[i+1]:
                if item in rucksack_list[i+2]:
                    sum2 = sum2 + priority[item]
                    break
    i=i+1
    counter = counter + 1
    if(counter==4):
        counter = 1

print(sum2)