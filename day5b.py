file = open('day5_input.txt', 'r')
stacks = []
crate_line = True
created = False
while True:
    try:
        # Lecture of the Crates
        line = file.readline()

        # Stacks Creation
        while not created:
            for i in range(int(len(line)/4)):
                stacks.append([])
            created = True

        # Crates registration
        if crate_line:
            crate_line = False
            for i in range(len(line)):
                if line[i] == '[':
                    crate_line = True
            if crate_line:
                for i in range(int(len(line)/4)):
                    if line[(4 * i) + 1] != ' ':
                        stacks[i].append(line[(4 * i) + 1])

        # Crates movement
        if line[0] == 'm':
            line = line.split(' ')
            for i in range(int(line[1])):
                stacks[int(line[5])-1].insert(i, stacks[int(line[3])-1][0])
                stacks[int(line[3])-1].pop(0)

    except(Exception,):
        for i in range(len(stacks)):
            print(stacks[i][0], end='')
        break
