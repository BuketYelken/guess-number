import random

guess = int(input("Welcome...\nYou have 3 chance, please take a guess number (0-1000): "))


number = random.randint(0, 1000)

key = 1

while(key < 4):
    if guess == number:
        print("Well done! Your guess is right.")
        key = 0
    elif guess > number:
        guess = int(input("Your guess over then number. Please guess again: "))
        key += key
    else:
        guess = int(input("Your guess less then number. Please guess again: "))
        key += key

print("Number: ", number)

