#  game of Hangman

import random

WORDS = ('python', 'game', )


def input_char():
    while True:
        user_input = input('Enter please a char ')
        if len(user_input) == 1:
            return user_input
        else:
            print('Enter please only one char ')


def is_char(char, word, correct_list, current_lives):
    if char in word:
        k = 0
        for i in word:
            if i == char:
                correct_list[k] = char
            k += 1
    else:
        current_lives -= 1
        print('dont have a char in word, the lives left ', current_lives)
    return correct_list, current_lives


def main():
    lives = 5
    word_index = random.randint(0, len(WORDS) - 1)
    game_word = WORDS[word_index]
    game_field = ['*'] * len(game_word)
    print('My word is', *game_field, '\nyou have {} lives'.format(lives))
    while True:
        if '*' not in game_field:
            print('You won!')
            break
        elif lives != 0:
            user_input = input_char()
            game_field, lives = is_char(user_input, game_word, game_field, lives)
            print('word is ', *game_field)
        else:
            print('Game Over')
            break


if __name__ == '__main__':
    main()
