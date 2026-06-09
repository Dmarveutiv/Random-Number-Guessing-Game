import random
import sys

if len(sys.argv) < 3:
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
else:
        first = sys.argv[1]
        second = sys.argv[2]

game = random.randint(int(first), int(second))

attempts = 0
while True:
    attempts += 1
    guess_num = int(input('Guess the number: '))
    if guess_num == game:
        print(f'You guessed the number! in {attempts} attempts.')
        break
    elif guess_num:
        x = int(game) - int(guess_num) 
        if x == 1:
            print('You are very close!')
    elif guess_num:
        x = int(guess_num) - int(game) 
        if x == 1:
            print('You are close!')
    else:
        print('Try again later!')