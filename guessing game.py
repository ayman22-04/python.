secret_number = 42
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("Game Over! You lost.")

print("Game Finished.")