#Trevor Payne 14 Arguments and Keyword Arguments

#arguments are declared within a function definition.  def MyFunc(arg1, arg2, ...)
#*args (star)args takes unlimited regular arguments.  They're placed in function argument to use.  Prevents program from crashing if we don't know how many arguments are passed.

def Func(*args):
	for eacharg in args:
		print(eacharg)
Func(1,2,3,54,"ham") #return 1\n2\n3\n54\nham

def Funclist(*args):
	for eacharg in args:
		print(eacharg)
alist = [1,2,3,54,"ham"]
Funclist(alist) #return [1, 2, 3, 54, 'ham'].  Function interprets one list as a whole.

def Funclist(*args):
	for eacharg in args:
		print(eacharg)
alist = [1,2,3,54,"ham"]
Funclist(alist[0],alist[1],alist[2]) #return 1\n2\n3 Pass each item in the list as one argument.
Funclist(*alist) #return 1\n2\n3\n54\nham.  Returns each item in the list.

#keyword arguments kwargs.  Declared variables within the arguments.  Use to set default values that may be overriden
def Funckwargs(x = 234, y = 9):  #x = 234, y = 9 are default values for function Funckwargs
	print(x, y)
Funckwargs(x = 456, y = 3) #return 456 3.  x and y defined in calling function Funckwargs overrides default values in function defintion.

def Funckkwargslist(**kwargs): #the double star means function treats values in a dictionary
	for eachitem in kwargs:
		print(eachitem)
Funckkwargslist(x = 789, y = -3) #return x and y or y and x

def Funckkwargslist(**kwargs): #the double star means function treats values in a dictionary
	for eachitem in kwargs.items():
		print(eachitem)
Funckkwargslist(x = 789, y = -3) #return ('y', -3) \n ('x', 789)

def Funccombine(*args, **kwargs):
	for eacharg in args:
		print(eacharg)
	for eachitem in kwargs.items():
		print(eachitem)
Funccombine("ham", 21, x = 456, y = 3) #return ham\n21\n('x', 456)\n('y', 3).  Arguments first, keyword arguments second because function define arguments first, keyword arguments second.