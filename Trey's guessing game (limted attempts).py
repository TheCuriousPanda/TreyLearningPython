#This is Trey's guessing game with limited number of tries!
###########################################################################
from random import randrange
import time
x=randrange(10)
solution=x
attempts=3
users = {
    'Spencer':'stp123',
    'Andrew':'penguin',
    'Trey':'gunso',
    'Morgan':'theflyingmo',
    'Celeste':'celestial1043'
    }
username=input("Please enter your username\n")
if (username in users):
    password=input("Please enter the password for user " + username + "\n")
    if (password == users[username]):
        print("Authorizing User...")
        time.sleep(3)
        print()
        print()
        print()
        print("User authorized! Please proceed and Good Luck!")
    else:
        print("Password incorrect")
        exit()
else:
    print("No user with that username")
    exit()
for numberofattempts in range(1,attempts+1):
    userguess=int(input("Guess a number between 1 and 10 \n"))
    if (userguess==solution):
        print()
        print("You are correct!")
        print()
        break
    if (userguess<solution):
        print()
        print("Sorry, that is incorrect, your guess is too low")
        print("You have", attempts-numberofattempts, "tries left")
        print()
    if (userguess>solution):
        print()
        print("Sorry, that is incorrect, your guess is too high")
        print("You have", attempts-numberofattempts, "tries left")
    if (attempts-numberofattempts==0):
        print()
        print("Sorry, the correct answer was", x)
        print("Better luck next time!")
        break
