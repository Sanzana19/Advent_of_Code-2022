file = open('day1_input.txt', 'r')

calories = []
elf_calories = 0

while True:
    try:
        line = file.readline()
        if line != '\n':
            elf_calories += int(line)
        else:
            calories.append(elf_calories)
            elf_calories = 0

    except (Exception,):
        calories.sort()
        print(sum(calories[-3:]))
        break
