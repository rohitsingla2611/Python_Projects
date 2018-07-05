import random

num1 = 40

to_be_guesses = int(num1 * random.random()) + 1
guess = 0

while guess != to_be_guesses:
    guess = int(input(' Enter a new guess number'))
    if 0 < guess < 20:
        if guess > to_be_guesses:
            print('Number too large')
        elif guess < to_be_guesses:
            print('Number too small')
    elif guess == to_be_guesses:
        print('You have made it')
    else:
        print('Sorry you are giving up!')
        break
