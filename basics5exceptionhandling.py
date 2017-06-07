#Trevor Payne Basics 5 of 8 Exception Handling

#exception handling prevents codes and scripts from breaking.  Can be used for handling user inputs.
#the keywords are "try", "except", "pass", "raise", "finally".  Try executes the code.  Except catches all erreors.  Pass says to ignore and move on may be used in For, While, Try/Except instances.  Raise forces an error to occur.  Finally always happens at the end before real errors returned.

#print(x = 5 + "ham") #error message appears.
#using try and except below, the print statement "Darn it" is executed
#instructor said good for debugging
try:
	x = 5 + "ham"
except:
	print("Darn it")

try:
	x = 6 + "ham"
except:
	pass

#raise TypeError("hahahaha")  #error message appears

try:
	x = 7 + "ham"
except ZeroDivisionError:
	print("will not see this")
finally:
	print("The final word")	#print The final word followed by the error TypeError:  unsupported operand type(s) . . . 