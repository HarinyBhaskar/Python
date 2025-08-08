import random

secret = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! The number was {secret}.")
        print(f"You guessed it in {attempts} tries.")
        break

