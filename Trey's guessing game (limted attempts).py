#This is Trey's guessing game with limited number of tries!
###########################################################################
attempts=3
solution=7
for numberofattempts in range(1,attempts+1):
	userguess=int(input("Guess a number between 1 and 10: "))
	if userguess==solution:
		print("You are correct!")
		break
	else:
		print("Sorry that is not correct")
		print("You have {} tries left".format(attempts-numberofattempts))