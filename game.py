"""A number-guessing game."""

# Put your code here
import random

print('hi')


name = input('what is your name? ')
print(f"hello {name}, I'm thinking of a number between 1 and 100")


def playgame():
    correct_num = random.randint(1, 100)
    count = 1
    try:
        guess = input('Your guess: ')
        if int(guess):
            while guess != correct_num:
                if int(guess) > correct_num:
                    print('too high')
                if int(guess) < correct_num:
                    print('too low')
                if int(guess) == correct_num:
                    print(f'congrats {name} thats the correct number!')
                    print(f'it took you {count} guesses!')
                    break
                count += 1
                guess = input('Your guess: ')

    except ValueError:
        print('please enter a integer, your count and number have been reset, do not break the rules or the rules will break you.')
        playgame()


playgame()
