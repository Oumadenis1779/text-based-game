import random

def secret_number():
    print("Welcome to the Secret Number Guessing Game!")
    print("I have chosen a secret number between 1 and 10. Try to guess it!")

    # Generate a random number between 1 and 10 for the secret number
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input("Enter your guess (between 1 and 10): "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You've guessed the secret number", secret_number, "correctly in", attempts, "attempts!")
            return  # End the game
        elif guess < secret_number:
            print("The secret number is higher than", guess)
        else:
            print("The secret number is lower than", guess)

    print("Sorry, you've run out of attempts. The secret number was", secret_number)

if __name__ == "__main__":
    secret_number()
