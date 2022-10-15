# Tic-tac-toe

import random


def make_field():
    new_field = list(range(1, 10))
    return new_field


def print_field(field):
    print('\n', field[0], '|', field[1], '|', field[2], '\n', field[3], '|', field[4], '|', field[5], '\n', field[6],
          '|', field[7], '|', field[8])


def can_move(field, position):
    if field[position] == 'x' or field[position] == 'o':
        return False
    else:
        return True


def user_input(field, marker):
    while True:
        user_position = int(input('\nEnter position to move '))
        if user_position in range(1, 10):
            if can_move(field, user_position - 1):
                field[user_position - 1] = marker
                print('\nYour move is:')
                return field
            else:
                print('You can not make that move ')
        else:
            print('You enter incorrect position ')


def comp_input(field, marker):
    while True:
        comp_position = random.randint(0, 8)
        if can_move(field, comp_position):
            field[comp_position] = marker
            print('\nComp move is:')
            return field


def is_game_finish(field):
    if (field[0] == field[1] == field[2] or field[3] == field[4] == field[5] or field[6] == field[7] == field[8] or
        field[0] == field[4] == field[8] or field[2] == field[4] == field[6] or field[0] == field[3] == field[6] or
            field[1] == field[4] == field[7] or field[2] == field[5] == field[8]):
        return True
    elif (field[0] != 1 and field[1] != 2 and field[2] != 3 and field[3] != 4 and field[4] != 5 and field[5] != 6
          and field[6] != 7 and field[7] != 8 and field[8] != 9):
        return True
    else:
        return False


def who_win(field):
    can_win = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    for i in can_win:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            winner = field[i[0]]
            return winner
    return 0


def main():
    first_move = random.randint(0, 1)
    if first_move == 0:
        print('First move user')
        marker = {'x': user_input, 'o': comp_input}
    else:
        print('First move comp')
        marker = {'o': user_input, 'x': comp_input}
    game_field = make_field()
    print_field(game_field)
    while not is_game_finish(game_field):
        game_field = marker['x'](game_field, 'x')
        print_field(game_field)
        if is_game_finish(game_field):
            break
        else:
            game_field = marker['o'](game_field, 'o')
            print_field(game_field)
    if who_win(game_field) == 0:
        print('Draw')
    elif who_win(game_field) == 'x':
        if first_move == 0:
            print('User win')
        else:
            print('Comp win')
    elif who_win(game_field) == 'o':
        if first_move == 1:
            print('User win')
        else:
            print('Comp win')


if __name__ == '__main__':
    main()
