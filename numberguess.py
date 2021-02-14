import random
 
hidden = random.randrange(1, 10)
print("Starting game")
 
guess = int(input("Please enter your guess: "))
 
if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")