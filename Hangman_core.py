from random import choice
from re import fullmatch


data_tuple = ('python', 'java', 'swift', 'javascript')
hello_message = 'H A N G M A N'
request_message = 'Input a letter: '


def check_input(guess_letter):
    if len(guess_letter) != 1:
        print('Please, input a single letter.')
    elif fullmatch(r'[a-z]', guess_letter):
        return True
    else:
        print('Please, enter a lowercase letter from the English alphabet.')


def play_round():
    secret_word = choice(data_tuple)
    print_word = ['-' for _ in range(len(secret_word))]
    suggested_letter = []
    attempt = 8
    while attempt != 0:
        print('\n', ''.join(print_word))
        guess_letter = input(request_message)
        if check_input(guess_letter):
            if guess_letter in suggested_letter:
                print("You've already guessed this letter.")
            else:
                suggested_letter.append(guess_letter)
                if guess_letter in set(secret_word):
                    for index, letter in enumerate(secret_word):
                        if letter == guess_letter:
                            print_word[index] = letter
                            if ''.join(print_word) == secret_word:
                                attempt = 0
                else:
                    print("That letter doesn't appear in the word.")
                    attempt -= 1
    if ''.join(print_word) == secret_word:
        print(f'You guessed the word {"".join(print_word)}!')
        print('You survived!')
        return True
    else:
        print('You lost!')
        return False


def main():
    scoreboard = {
        True: 0,
        False: 0,
    }
    menu_message = 'Type "play" to play the game, ' \
                   '"results" to show the scoreboard, and "exit" to quit:'
    print(hello_message)
    while True:
        player_choose = input(menu_message)
        if player_choose in ('play', 'results', 'exit'):
            if player_choose == 'exit':
                break
            elif player_choose == 'play':
                scoreboard[play_round()] += 1
            else:
                print(f'You won: {scoreboard[True]} times.')
                print(f'You lost: {scoreboard[False]} times.')


if __name__ == "__main__":
    main()
