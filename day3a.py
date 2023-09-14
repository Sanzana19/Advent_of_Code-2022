file = open('day3_input.txt', 'r')
priority_sum = 0

while True:
    rucksack = file.readline()
    checked = []
    for i in range(len(rucksack)//2):
        if (rucksack[i] in rucksack[len(rucksack)//2:]) and (rucksack[i] not in checked):
            if ord(rucksack[i]) > 90:
                priority_sum += ord(rucksack[i]) - 96  # Lowercase
            else:
                priority_sum += ord(rucksack[i]) - 38  # Uppercase
        checked.append(rucksack[i])
    if rucksack == '':
        print(priority_sum)
        break
