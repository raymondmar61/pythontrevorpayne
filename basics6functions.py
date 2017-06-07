#Trevor Payne Basics 6 of 8 Functions

#functions are ways to combine many actions into a single process to reuse later
#def defines or declare a function.  The paranthesis is the input or arguments passed in the paranthesis.  The main code is below the def statement.
def functionname():
	pass
functionname() #call a function.  Type the function name.

#return keyword.  return is a way to output or return data from a function.  Get something back from the function.
def makeone():
	return 1
print(makeone()) #print 1

#arguments inside the paranthesis pass information into a function.  A way to input or pass in data to a function.  Input or arguments is gas; output or return is drive the car.
#there are two types of arguments:  regular and keyword or default value.  e.g. def myFunc(var1, var2 = 3) for which regular is var1 on the left, keyword or default value is var2 on the right.
def addten(myint):
	myint += 10
	return myint
print(12, addten(12)) #print 12 22

#document string.  Do I need to know?
def myfunc():
	'''three single quotes typed immediately after function declaration is a document string.  Access function declaration print(functionname.__doc__)'''
	#Comments only seen in code view.  Computer ignores it.
	pass
print(myfunc())
print(myfunc.__doc__)