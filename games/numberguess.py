# Number guessing game
import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    guess_the_number()