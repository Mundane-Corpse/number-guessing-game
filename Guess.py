secret = 7
guess = int(input("Guess the secret number: "))
while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess the secret number: "))
print("Congratulations! You guessed the secret number.")