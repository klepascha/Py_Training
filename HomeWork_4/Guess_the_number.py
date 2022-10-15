# Guess the number

import random


def user_input():
    while True:
        user_number_input = input('Please enter integer number ')
        try:
            return int(user_number_input)
        except ValueError:
            print('Incorrect enter')


def is_game_finish(user_number, correct_number):
    if user_number == correct_number:
        print('You guessed the number! Congratulation!')
        return True
    elif user_number > correct_number:
        print('Your number is bigger')
        return False
    else:
        print('Your number is lower')


def main():
    guess_number = random.randint(1, 100)
    print(guess_number)
    while True:
        user_num = user_input()
        if is_game_finish(user_num, guess_number):
            break


if __name__ == '__main__':
    main()
