from random import randint
machine_number = randint(1,10)
guess = int(input("Guess the number: "))
print(machine_number)

for guesses in range(1,5):
    if guess < machine_number:
        guess = int(input(f"{guess} is less than my number. Try again: "))
    elif guess > machine_number:
        guess = int(input(f"{guess} is greater than my number. Try again: "))
    else:
        print(f"You won.{guess} is my number.")
        break

if guess != machine_number:
    print(f"You lost. {machine_number} is my number,")