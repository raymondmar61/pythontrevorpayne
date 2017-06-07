#Trevor Payne 1 Integers Floats and Maths, 2 Strings Lists Tuples Dictionaries, 3 Conditionals If Else Elif, 4 Loops, 5 Exception Handling, 6 Functions, 7 Files and User Input, 8 Classes, 9 Creating Text Files, 10 Inheritance OOP, 11 Overriding File Manager, 14 Args Kwargs, 15 Nesting Functions Decorators, 16 Singletons

print(32/32) #print 1.0
print(32//32) #print 1
print(int(32/32)) #print 1
print(3/2) #print 1.5
print(3/2.0) #print 1.5
print(int(3/2.0)) #print 1
print(round(3/2.0)) #print 2
print(round(1.2345734324,4)) #print 1.2346
print(abs(-9)) #print 9
import math
print(math.floor(2.5)) #print 2
print(math.ceil(2.5)) #print 3
print(pow(5,2)) #print 25
print("\n")

x = "hamsandwich"
print(x + " book") #print hamsandwich book
z = 10
print(x + " "+str(z)) #print hamsandwich 10
print("something %d" %z) #print something 10.  %d represents integers
print("something %f" %z) #print something 10.000000  %f represents floats
print("something %.3f" %z) #print something 10.000  %.nf represents number of digits
print("test\tpest") #print test    pest
xlist = ["ham",4,2.2]
print(xlist) #print ['ham', 4, 2.2]
xlist.append(5)
print(xlist) #print ['ham', 4, 2.2, 5]
xlist.insert(1,3.1415)
print(xlist) #print ['ham', 3.1415, 4, 2.2, 5]
xlist.pop(1) #removes item index #1
print(xlist) #print ['ham', 4, 2.2, 5]
print(len(xlist)) #print 4
print(list("ham")) #print ['h', 'a', 'm']
ylist = []
ylist.append("ham")
print(ylist) #print ['ham']
print("s" in ylist) #print False
xtuple = ("ham",4, 5)
print(xtuple) #print ('ham',4, 5)
xdictionary = {"weapon":"chainsaw", "health":10}
print(xdictionary) #print {'health': 10, 'weapon': 'chainsaw'}
print(xdictionary["weapon"]) #print chainsaw
del xdictionary["health"]
print(xdictionary) #print {'weapon': 'chainsaw'}
xdictionary.update({"health": 20}) #source is williamfiset
print(xdictionary) #print {'health': 20, 'weapon': 'chainsaw'}
#reminder dictionary printing sort is not important
print("\n")

mail = 5
if mail:
	print("mail time") #print mail time
mail = 0
if mail:
	print("mail time")
else:
	print("no mail") #print no mail
if (4 < 6):
	print("ham sandwich") #print ham sandwich
if (7 <= 6):
	print("whaaaa")
else:
	print("7 is greater than 6") #print 7 is greater than 6
if (7) and (6): #or keyword is also valid
	print("yep") #print yep
if (0) and (4):
	print("wahaaa") #print nothing
if not (0):
	print("yup") #print yup
print("\n")

x = 0
while (x < 10):
	print(x)
	x +=1
x = 0
y = 0
while (True):
	x+=1
	y+=2
	z = x + y
	if (x + y > 10):
		break
	print(str(x)+ "+" +str(y)+"= %i" %z)
x = [1, 2, 7]
for eachx in x:
	print(eachx)
for eachnumber in range(30, 10, -2): #range(min, max-1, step size)
	print(eachnumber)
for eachrange in range(0,30):
	if not (eachrange % 3 != 0): #I added !=0 to avoid confusion
		continue
	print(eachrange)
print("\n")

try:
	x = 5 + "ham"
except:
	print("darn it-->unsupported operand type(s) for +: 'int' and 'str'")
try:
	x = 5 + "ham"
except:
	pass
#raise TypeError("hahahaha") #return actual error-->TypeError: hahahaha.  Raise force an error to occur
#Finally is the last action to perform after try and except.  Occurs before any real errors are returned.
try:
	x = 5 + "ham"
except ZeroDivisionError:
	print("Nobody sees the ZeroDivisionError print statement because the error is not ZeroDivisionError.  It's a TypeError.")
except TypeError:
	print("It's a TypeError.")
finally:
	print("Everybody sees the finally final word no matter what.  Correct?")
print("\n")

def doesNothing():
	pass
doesNothing()
def makeOne():
	return 1
print(makeOne()) #print 1
def addTen(myInt):
	myInt +=10
	return myInt
x = 12
print(addTen(x)) #print 22
def myFunc():
	'''The document string I documented something for the function myFunc()'''
	#Only seen in code view, computer ignores
	pass
print(myFunc.__doc__) #print The document string I documented something for the function myFunc()
print("\n")

highest = 10
answer = 7
guess = input("Guess a number from 0 to %d: " %highest)
while(int(guess) != int(answer)):
	if (int(guess) < int(answer)):
		print("Answer is higher")
	elif (int(guess) > int(answer)):
		print("Answer is lower")
	else:
		print("Correct") #print the correct statement outside the while loop.  I wonder why print("Correct") is not printed?  It was before pass keyword.  03/31/17.  I believe when answer is correct, Python leaves the while loop.
		pass
	guess = input("Guess a number from 0 to %d: " %highest)
print("Correct2") #print Correct2

""" comment while loop below for easy use
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
"""

import basics7ph #get the basics7ph file
for eachnumber in range(0,10):
	basics7ph.printham() #print ham in its own line
	print(eachnumber) #print numbers 0 to 9 in its own line
print("\n")

class Test:
	pass
x = Test()
class Ph:
	def printHam(self):
		print("hamclass")
x = Ph()
x.printHam() #return hamclass
class Ph2():
	def __init__(self):
		self.y = 5		
x2 = Ph2()
print(x2.y) #print 5.  It's like self.y=5<-->x2.y=5.
class Ph3:
	def __init__(self):
		self.y = 5
		self.printHam()	
	def printHam(self):
		print("hamclass3")
x3 = Ph3() #return hamclass3 because self.printHam() called printHam()
class Hero:
	def __init__(self, name):
		self.name = name
		self.health	 = 100
	def eat(self, food):
		if (food == "apple"):
			self.health -= 100
		elif (food == "ham"):
			self.health += 20
Bob = Hero("Bob")			
print(Bob.name) #print Bob
print(Bob.health) #print 100
Bob.eat("apple") #Bob eats apple.  food variable is apple.
print(Bob.health) #print 0
print("\n")

''' comment creating a text file below for easy use
import time as t
from os import path #path checks file if not already created.  No overwriting.
def createFile(dest):
	''''The script creates a text file at the passed in location, names file based on date''''''
	#print(dest) #print statement used to dest createFile () function
	date = t.localtime(t.time()) #get current time/date and save to date
	#FileName = Month_Date_Year.txt
	print(date) #time.struct_time(tm_year=2016, tm_mon=7, tm_mday=19, tm_hour=17, tm_min=43, tm_sec=21, tm_wday=1, tm_yday=201, tm_isdst=1)
	name = "%d_%d_%d.txt" % (date[1], date[2], (date[0] % 100)) #output in month_date_year.txt format
	if not (path.isfile(dest + name)): #checks if file already exists.  If not, then create file
		filenew = open(dest + name, "w")
		filenew.write("\n"*30) #write a new line 30 times
		filenew.close()
if (__name__ == "__main__"): #if file name main or the file is the main file, then call function createFile(dest)
	#destination varabile is location file to be saved
	destination = "/home/mar/Python/trevorpayne/"
	createFile(destination) #createFile(destination).  Call function createFile() passing destination to dest
	input("done!!!") #raw_input doesn't work in python 3.5.  Use input("done!!!")
'''
print("\n")

class BaseClass(object):
	def printHam(self):
		print("ham from BaseClass")
class InheritingClass(BaseClass):
	pass
x = InheritingClass()
x.printHam() #return ham from BaseClass
class Character(object):
	def __init__(self, name):
		self.health = 100
		self.name = name
	def printName(self):
		print(self.name)
class Blacksmith(Character):
	def __init__(self, name, forgeName):
		super(Blacksmith, self).__init__(name) #calls the init function of Base Class which is Character
		self.forge = Forge(forgeName)
class Forge:
	def __init__(self, forgeName):
		self.name = forgeName
bs = Blacksmith("Bob","Rick\'s forge")
bs.printName() #print Bob
print(bs.forge.name) #print Rick's forge.  bs<-->Blacksmith() self.forge<-->bs.forge self.name<-->bs.name???
print("\n")

class BaseClass(object):
	def __init__(self):
		self.x = 10
class InheritanceClass(BaseClass):
	def __init__(self):
		super(InheritanceClass, self).__init__()
		self.x = 20
i = InheritanceClass()
print(i.x) #print 20  It's like self.x=20<-->i.x=20.
class BaseClass2(object):
	def test(self):
		print("ham from BaseClass2")	
class InheritanceClass2(BaseClass2):
	def test(self):
		print("hammer time from BaseClass2")
i2 = InheritanceClass2()
i2.test() #return hammer time from BaseClass2
print("\n")

def Func(*args):
	for eacharg in args:
		print(eacharg)
Func(1,2,3,54,"ham") #return 1\n2\n3\n54\nham
Func([1,2,3,54,"ham"]) #return [1,2,3,54,"ham"]
listargs = [1,2,3,54,"ham"]
Func(*listargs) #return 1\n2\n3\n54\nham
def Funckwargs(x=234, y = 9):
	print(x, y)
Funckwargs() #return 234 9
Funckwargs(456,3) #return 456 3
def Funckwargslist(**kwargs):
	for item in kwargs.items():
		print(item)
Funckwargslist(x = 456, y = 3) #return ('y', 3)\n('x', 456)
def Funckwargslistcombined(*args, **kwargs):
	for eacharg in args:
		print(eacharg)
	for item in kwargs.items():
		print(item)
Funckwargslistcombined("ham", 21, x = 456, y = 3) #return ham\n21\n('x', 456)\n('y', 3).  Arguments first, keyword arguments second because function define arguments first, keyword arguments second.
print("\n")

def Outsidefunction():
	def Insidefunction():
		print("blah")
	return Insidefunction
myFunc = Outsidefunction()
myFunc() #return blah
def Outsidefunction():
	x = 5
	def Insidefunction(): #Inside() takes a snapshot of all variables Inside() has access.  x = 5 is a global variable for Inside(), it stores in the snapshot.  It's like Outside() is a class.
	#Why not use a class?  Less code than classes.  Don't need to know what function you're calling, just take on "()".  Can use "If, Else, Elif" to choose which function is returned.
		print(x)
	return Insidefunction
myFunc = Outsidefunction()
myFunc() #return 5
def Outside(x = 5):
	def Inside():
		print(x)
	return Inside
myFunc = Outside(3456)
myFunc() #return 3456
def addOne(myFunc):
	def addOneInside():
		return myFunc() + 1
	return addOneInside
def oldFunc():
	return 3
newFunc = addOne(oldFunc)
print(oldFunc(), newFunc()) #return 3 4

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
print("\n")

class MySingleton(object):
	_instance = None
	def __new__(self):
		if not self._instance:
			self._instance = super(MySingleton, self).__new__(self)
			self.y = 10
		return self._instance
x = MySingleton() #create instance
print(x.y) #print 10
x.y = 20 #change value
z = MySingleton() #access instance
print(z.y) #print 20
print(x.y) #print 20
def singleton(myClass):
	instances = {}
	def getInstance(*args,**kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args,**kwargs)
		return instances[myClass]
	return getInstance
@singleton
class TestClass(object):
	pass
x = TestClass()