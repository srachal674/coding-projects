import random

num = random.randint(1, 20)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    tries = tries + 1
    
    if guess > num:
        print("Too high! Try again")
        
    elif guess < num:
        print("Too low! Guess again.")
        
    else:
        print("You got it!")
        print("It took you ", tries, " tries to guess the number.")
        break
    

