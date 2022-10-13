# -*- coding: utf-8 -*-
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

NOT_CAN_MOVE = {
    'w': (0, 1, 2, 3),
    's': (15, 14, 13, 12),
    'a': (0, 4, 8, 12),
    'd': (3, 7, 11, 15)
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    result_fild = list(range(1, 16)) + list(EMPTY_MARK)
    random.shuffle(result_fild)
    return result_fild


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    print('\n', field[0:4], '\n', field[4:8], '\n', field[8:12], '\n', field[12:16])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    result_fild = list(range(1, 16)) + list(EMPTY_MARK)
    return field == result_fild


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't be done.
    """
    for pole in field:
        if pole == EMPTY_MARK:
            index = field.index(pole)
            if index in NOT_CAN_MOVE[key]:
                raise IndexError("The move can't be done")
            else:
                field[index], field[index + MOVES[key]] = field[index + MOVES[key]], field[index]
                break
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    print("""\nPlease, enter your move:
    'w' - up, 
    's' - down,
    'a' - left, 
    'd' - right
    """)
    while True:
        user_input = input('Your move is: ')
        if user_input in MOVES:
            return user_input
        elif user_input == 'exit':
            raise KeyboardInterrupt('Goodbye!')
        else:
            print('You enter incorrect move, try again!')


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    print('\nThe Game is started. If you want to exit enter "exit" in your move')
    game_field = shuffle_field()
    print_field(game_field)
    try:
        while not is_game_finished(game_field):
            try:
                user_input = handle_user_input()
                perform_move(game_field, user_input)
                print_field(game_field)
            except IndexError as err:
                print(err)
                print_field(game_field)
        print('\nYou  won!!!')
    except KeyboardInterrupt as err:
        print(err)


if __name__ == '__main__':

    main()
