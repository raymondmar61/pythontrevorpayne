#Trevor Payne Basics 7 of 8 Files and User Input

highest = 10
answer = 7
guess = input("Guess a number from 0 to %d: " %highest)
while(int(guess) != int(answer)):
	if (int(guess) < int(answer)):
		print("Answer is higher")
	elif (int(guess) > int(answer)):
		print("Answer is lower")
	else:
		print("Correct") #print the correct statement outside the while loop.  I wonder why print("Correct") is not printed?  It was before pass keyword.
		pass
	guess = input("Guess a number from 0 to %d: " %highest)
print("Correct2") #print Correct2

import random
highest = 10
answer = random.randrange(0,highest) #random range.  Gets a random number from 0 to, in this case, highest which is 10.
guess = input("Guess a number from 0 to %d: " %highest)
while(int(guess) != int(answer)):
	if (int(guess) < int(answer)):
		print("Answer is higher")
	elif (int(guess) > int(answer)):
		print("Answer is lower")
	else:
		print("Correct") #print the correct statement outside the while loop.  I wonder why print("Correct") is not printed?  It was before pass keyword.
		pass
	guess = input("Guess a number from 0 to %d: " %highest)
print("Correct3") #print Correct3



