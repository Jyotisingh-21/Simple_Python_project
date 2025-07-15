import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Your guess is Low')
        elif guess > random_num:
            print('Your guess is High')
    print("Congrats you guessed it!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H) , too low (L), or correct (C)')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1

    print('I got it!')

computer_guess(2)
