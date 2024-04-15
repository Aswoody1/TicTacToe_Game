rows = {'A': ['A', '___', '___', '___'], 'B': ['B', '___', '___', '___'], 'C': ['C', '___', '___', '___']}


def check_result():
    if rows['A'][1] == rows['A'][2] == rows['A'][3] == ' X ' or rows['B'][1] == rows['B'][2] == rows['B'][
        3] == ' X ' or rows['C'][1] == rows['C'][2] == rows['C'][3] == ' X ' or rows['A'][1] == rows['B'][2] == \
            rows['C'][3] == ' X ' or rows['A'][3] == rows['B'][2] == rows['C'][1] == ' X ' or rows['A'][1] == \
            rows['B'][1] == rows['C'][1] == ' X ' or rows['A'][2] == rows['B'][2] == rows['C'][2] == ' X ' or \
            rows['A'][3] == rows['B'][3] == rows['C'][3] == ' X ':
        print(f'Congratulations player 1, you won.\n')
        return True
    elif rows['A'][1] == rows['A'][2] == rows['A'][3] == ' O ' or rows['B'][1] == rows['B'][2] == rows['B'][3] == ' O ' or rows['C'][1] == rows['C'][2] == rows['C'][3] == ' O ' or rows['A'][1] == rows['B'][2] == \
            rows['C'][3] == ' O ' or rows['A'][3] == rows['B'][2] == rows['C'][1] == ' O ' or rows['A'][1] == \
            rows['B'][1] == rows['C'][1] == ' O ' or rows['A'][2] == rows['B'][2] == rows['C'][2] == ' O ' or \
            rows['A'][3] == rows['B'][3] == rows['C'][3] == ' O ':
        print(f'Congratulations player 2, you won.\n')
        return True
    else:
        count = 0
        for row in rows:
            for element in rows[row]:
                if element != '___':
                    count += 1
                    if count == 12:
                        print(f"It's a draw. You're going to have to play again if you want to find who's truly "
                              f"intellectually superior.\n")
                        return True
                elif element == '___':
                    return False


def player_1_turn():
    row = input('Player 1, which row (horizontal) would you like to place your cross? (e.g. A, B, C) \n').upper()
    column = int(input('and which column (vertical) would you like to place your cross? (e.g. 1, 2, 3) \n'))
    if rows[row][column] == '___':
        rows[row][column] = ' X '
    else:
        print("There's already a marker there, try again.\n")
        player_1_turn()


def player_2_turn():
    row = input('Player 2, which row (horizontal) would you like to place your nought? (e.g. A, B, C) \n').upper()
    column = int(input('and which column (vertical) would you like to place your nought? (e.g. 1, 2, 3) \n'))
    if rows[row][column] == '___':
        rows[row][column] = ' O '
    else:
        print("There's already a marker there, try again.\n")
        player_2_turn()


def show_board():
    print(f"\n{rows['A']}")
    print(rows['B'])
    print(f"{rows['C']}\n")


def play_game():
    show_board()
    game_on = True
    while game_on:
        player_1_turn()
        show_board()
        if check_result():
            game_on = False
        else:
            player_2_turn()
            show_board()
            if check_result():
                game_on = False


play_game()
