#Trevor Payne Basics 8 of 8 Classes

#classes are a way of packaging variables and functions together
#class Classname: pass
#class is the keyword to begin a class.  Always capitalize first letter of class name.
#self keyword used to attach variables and functions to a class
class Test:
	pass
x = Test() #Create class instance is just like calling a function

class Testself:
	def printham(self):
		print("ham")
Testself().printham() #return ham.  Works without declaring variable to the class Testself.  In this example, declaring variable is x.
x = Testself()
x.printham() #return ham
print("\n")

#initialization or constructor.  Function run when class instance created.
class Testself2:
	def __init__(self):
		self.y = 5
	def printham(self):
		print("ham2")
Testself2().printham() #return ham2.  Works without declaring variable to the class Testself2.  In this example, declaring variable is x2.
x2 = Testself2()
x2.printham() #return ham2
print(x2.y) #print 5
print("\n")

class Testself3:
	def __init__(self):
		self.y = 6
		self.printham()
	def printham(self):
		print("ham3")
Testself3().printham() #return ham3\nham3.  Works without declaring variable to the class Testself3.  In this example, declaring variable is x3.  Why did ham3 print twice?  I think self.printham() calls def printham(self) for one print ham3.
x3 = Testself3() #return ham3
x3.printham() #return ham3
print(x3.y) #print 6
print("\n")

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