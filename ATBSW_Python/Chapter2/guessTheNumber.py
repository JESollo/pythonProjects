#this is a guess the number game

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for takenGuess in range(1,4):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your number is too low.')
    elif guess > secretNumber:
         print('Your number is too high.')
    else:
        break

if guess == secretNumber:
    print('You guessed the correct number! You guessed your number ' + str(takenGuess) + 'guesses!')
else:
    print('Sorry. The number I was thinking of was ' + str(takenGuess))
