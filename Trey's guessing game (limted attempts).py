#This is Trey's guessing game with limited number of tries!
###########################################################################
attempts=3
solution=7
password=input("Please enter the password to access this game \n")
if (password=="Python"):
    print("That is correct! Please procced and good luck!")
else:
    print("Sorry that is incorrect, goodbye")
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
        print("Sorry, no more tries left, goodbye")
        break

        
