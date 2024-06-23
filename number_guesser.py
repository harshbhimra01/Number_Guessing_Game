import random
number = input("Enter your number: ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print("Enter a number greater then 0")
        quit()
    elif number >= 101:
        print("Enter a number smaller then 100")
        quit()
else:
    print("Please enter a valid number")
    quit()

random = random.randrange(number)
guess_count = 0

while True:
    guess_count += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Try again")
        continue

    if guess == random:
        print("You got it! ")
        break
    elif guess > random:
        print("You are above")
    else:
        print("You are below")

print("Your get it in", guess_count, "guess")