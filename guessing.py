import random
from tokenize import Number

numbers=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("enter your guess"))
    if guess==numbers:
        print("You Won")
    elif guess<numbers:
        print("your guess was too low")
    else :
        print("your guess is to high")
    chances=chances+1 

if not chances<5:
    print("You Loose",numbers)       