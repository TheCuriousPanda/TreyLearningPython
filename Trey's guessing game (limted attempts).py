#This is Trey's guessing game with limited number of tries!
###########################################################################
from random import randrange
import time
import UserFileEditor
x=randrange(10)
solution=x+1
attempts=3
users = UserFileEditor.read_users()
usernames = []
for user in users:
    usernames.append(user.get_name())
stringinputs = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10
    }
    
username=input("Please enter your username or \"new\" for new user\n")
#if (username="new"):
#    
if (username in usernames):
    passcheck = users[usernames.index(username)].get_password()
    password=input("Please enter the password for user " + username + "\n")
    if (password == passcheck):
        print("Authorizing User...")
        time.sleep(1)
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
    userguess=input("Guess a number between 1 and 10 \n")
    try:
        userguess=int(userguess)
    except ValueError:
        if (userguess.lower() in stringinputs):
            userguess=stringinputs[userguess.lower()]
        else:
            print("Not a valid string input")
            break
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
        print("Sorry, the correct answer was {}".format(solution))
        print("Better luck next time!")
        break
