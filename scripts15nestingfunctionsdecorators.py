#Trevor Payne 15 Nesting Functions And Decorators

#nesting functions are functions declared within other functions.  Works because functions are just objects.
#When you define a function, it's stored in python just like a class or variable as an object
#Since functions are just like variables, they can be returned from a function

def Outside():
	def Inside():
		print("blah")
	return Inside
myFunc = Outside()
myFunc() #return blah

def Outside():
	x = 5
	def Inside(): #Inside() takes a snapshot of all variables Inside() has access.  x = 5 is a global variable for Inside(), it stores in the snapshot.  It's like Outside() is a class.
	#Why not use a class?  Less code than classes.  Don't need to know what function you're calling, just take on "()".  Can use "If, Else, Elif" to choose which function is returned.
		print(x)
	return Inside
myFunc = Outside()
myFunc() #return 5

#example passing in arguments and local copy made
def Outside(x = 5):
	def Inside():
		print(x)
	return Inside
myFunc = Outside(3456)
myFunc() #return 3456

#Functions are objects just like variables
#Let's pass a function as an argument into another function
def addOne(myFunc):
	def addOneInside():
		return myFunc() + 1
	return addOneInside
def oldFunc():
	return 3
newFunc = addOne(oldFunc)
print(oldFunc(), newFunc()) #return 3 4
#addOne() takes oldFunc() value 3 saved in variable newFunc and addOne() function receives value 3 saved as myFunc.  Call addOne() function giving it oldFunc() value 3.
#addOneInside() function takes myFunc = 3 and adds one returning 4 from addOneInside() and then returning addOne by storing 4 in addOneInside

#Decorators.  Adds something to an existing function.
def addOne(myFunc):
	def addOneInside():
		return myFunc() + 1
	return addOneInside
def oldFunc():
	return 3
oldFunc = addOne(oldFunc)
print(oldFunc()) #print 4

def addOne(myFunc):
	def addOneInside():
		return myFunc() + 1
	return addOneInside
@addOne #@ symbol before definition of function is a Decorator.  Says pass the oldFunc() and add something with the addOne() function.  Override the previous oldFunc() = 3 value.
def oldFunc():
	return 3
print(oldFunc()) #print 4

def addOne(myFunc):
	def addOner(*args, **kwargs):
		return myFunc(*args, **kwargs) + 1
	return addOner
@addOne	
def oldFunc(x = 3245):
	return x
print(oldFunc()) #print 3246
print(oldFunc(500)) #print 501

