userguess=input("Please enter something: ")
#if userguess==str(input()):
#    print("The sentence you have enter is a string input")
try:
    intguess=int(userguess)
except ValueError:
    intguess = "You did not input an integer"
print(intguess)
