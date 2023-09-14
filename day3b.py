file = open('day3_input.txt', 'r')
priority_sum = 0

while True:
    rucksack_1 = set(file.readline())
    rucksack_2 = set(file.readline())
    rucksack_3 = set(file.readline())

    checked = rucksack_1 & rucksack_2  # Items from first rucksack in second rucksack
    checked = checked & rucksack_3  # Items in all rucksacks
    checked -= {'\n'}

    for i in checked:
        item = i
        if ord(item) > 90:
            priority_sum += ord(item) - 96  # Lowercase
        else:
            priority_sum += ord(item) - 38  # Uppercase

    if rucksack_1 == set():
        print(priority_sum)
        break
