from random import randint
machine_number = randint(1,10)
guesses = 1
guess = int(input("Guess the number: "))
#print(machine_number)

while guesses <5 and guess != machine_number:
    guesses += 1
    if guess < machine_number:
        guess = int(input("My number is greater. Please try again: "))
    else:
        guess = int(input("My number is less. Please try again: "))

if guess == machine_number:
    print(f"You won.{guess} is my number.")
else:
    print(f"You lost.{machine_number} is my number.")


