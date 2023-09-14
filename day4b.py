file = open('day4_input.txt', 'r')
pairs = 0

while True:
    try:
        elf_pair = file.readline().split('\n')
        elf_pair = elf_pair[0].split(',')
        elf_pair = elf_pair[0].split('-'), elf_pair[1].split('-')

        a = set(range(int(elf_pair[0][0]), int(elf_pair[0][1])+1))
        b = set(range(int(elf_pair[1][0]), int(elf_pair[1][1])+1))

        if a & b != set() or a & b != set():
            pairs += 1

    except(Exception,):
        print(pairs)
        break
