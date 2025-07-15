import random
from termcolor import colored
from words import words

def get_target_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def get_feedback(guess, target):
    feedback = []
    guess = guess.upper()
    target = target.upper()
    
    for i in range(5):
        letter = guess[i]
        if letter == target[i]:
            # Green for correct letter & position
            feedback.append(colored(letter, 'green', attrs=['bold']))
        elif letter in target:
            # Yellow for correct letter, wrong position
            feedback.append(colored(letter, 'yellow', attrs=['bold']))
        else:
            # Gray for wrong letter
            feedback.append(colored(letter, 'white'))
    
    return ' '.join(feedback)

def wordle():
    target = get_target_word().upper()
    attempts = 6

    while attempts > 0:
        guess = input("Enter your guess word: ").strip().upper()
        if len(guess) != 5 or not guess.isalpha():
            print("❌ Please enter any five-letter word using alphabet letters only.")
            continue

        feedback = get_feedback(guess, target)
        print(f"Your guess: {guess}")
        print(f"Feedback: {feedback}")

        if guess == target:
            print("🎉 Congratulations! You guessed the word!")
            break

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    if guess != target:
        print(f"😞 Game over. The word was: {target}")


wordle()