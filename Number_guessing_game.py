import random

print("Hello! Welcome to the Number Guessing Game.\nHere, You have 7 chances to guess the number. Let's start and play!")

lower_number = int(input("Enter the Lower Bound Number: "))
higher_number = int(input("Enter the Upper Bound Number: "))

print(f"\nYou have 7 chances to guess the number between {lower_number} and {higher_number}. Let's start and play!")

num = random.randint(lower_number, higher_number) 
ch = 7                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'orry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')