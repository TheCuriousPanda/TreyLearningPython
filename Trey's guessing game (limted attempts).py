#This is Trey's guessing game with limited number of tries!
###########################################################################
attempts=3
solution=7
for numberofattempts in range(1,attempts+1):
    userguess=int(input("Guess a number between 1 and 10 \n"))
    if (userguess==solution):
        print()
        print("You are correct!")
        print()
        break
    else:
        print("Sorry, that is incorrect")
        print()
        print("You have", attempts-numberofattempts, "tries left")
        print()
    if (attempts-numberofattempts==0):
        print("Sorry, no more tries left, goodbye")
        
