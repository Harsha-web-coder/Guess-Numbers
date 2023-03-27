import random

def guess(x):
    random_number = random.randint(1, x)
    score=100
    guess = 0
    print("CONDITION IS:")
    print("maxScore is 100 & for every incorrect score decrease by 10")
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
            score-=10
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
            score-=10

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
    print("Your score is:",score)
"""
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
"""
guess(10)
"""
OUTPUT:
Guess a number between 1 and 10: 5
Sorry, guess again. Too low.
Guess a number between 1 and 10: 7
Sorry, guess again. Too high.
Guess a number between 1 and 10: 6
Yay, congrats. You have guessed the number 6 correctly!!
"""