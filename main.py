import random

secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You have guessed it - congratulations! Its number " + str(secret) + ".")
        break
    elif guess > secret:
        print("Try something smaller.")
    elif guess < secret:
        print("Try something bigger.")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))