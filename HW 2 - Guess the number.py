from random import randint
machine_number = randint(1,10)
guess = int(input("Guess the number: "))

if guess == machine_number:
    print(f"Congrats. {guess} is the number")
elif guess > machine_number:
    print(f"{guess} is greater than the number.")
    guess_again = int(input("Try again: "))
else: #guess < machine_number
    print(f"{guess} is less than the number.")
    guess_again = int(input("Try again: "))

if guess_again == machine_number:
    print(f"Congrats. {guess_again} is the number")
else:
    print("You lost.")
