file = open('day1_input.txt', 'r')

max_calories_carried = 0
elf_calories = 0

while True:
    try:
        line = file.readline()
        if elf_calories > max_calories_carried:
            max_calories_carried = elf_calories
        if line != '\n':
            elf_calories += int(line)
        else:
            elf_calories = 0

    except (Exception,):
        print(max_calories_carried)
        break
