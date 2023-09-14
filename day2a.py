file = open('day2_input.txt', 'r')

score = 0

while True:
    try:
        game_round = file.readline()

        # Shape points
        match game_round[2]:
            case 'X': score += 1  # Rock
            case 'Y': score += 2  # Paper
            case 'Z': score += 3  # Scissors

        # Outcome points
        if (game_round[2] == 'X' and game_round[0] == 'A') or \
           (game_round[2] == 'Y' and game_round[0] == 'B') or \
           (game_round[2] == 'Z' and game_round[0] == 'C'):
            score += 3  # Draw

        if (game_round[2] == 'X' and game_round[0] == 'C') or \
           (game_round[2] == 'Y' and game_round[0] == 'A') or \
           (game_round[2] == 'Z' and game_round[0] == 'B'):
            score += 6  # Win

    except (Exception,):
        print(score)
        break
