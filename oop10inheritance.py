#Trevor Payne 10 OOP 1 of 3 Inheritance

#Object Oriented Programming (OOP)
#OOP is programming based around classes and instances of those classes aka Objects
#Revolves around how classes interact and directly affect one another
#Today we focus on Inheritance.  One classes acquires attributes from another class.
#OOP is a cleaner way of programming.  Changes to the Base class affect all classes which inherit from the Base class.

class BaseClass(object):  #create class Baseclass inheriting from object.  Object is a Base class stored somewhere in the same file.
#(object) allows you to call the __init__ function from Baseclass.  An inheriting class calling Baseclass's __init__.  Instructor says keep (object) which allows access to Baseclass variables.
	def printHam(self):
		print("ham")
class InheritingClass(BaseClass): #create class InheritingClass inheriting from BaseClass
	pass
x = InheritingClass()
x.printHam() #return ham

class Character(object): #Character is the Base class
	def __init__(self):  #init calls the constructor
		self.health = 100
class Blacksmith(Character):  #Blacksmith is the Inheriting class.  It's inheriting the Base class Character
	def __init__(self): #init class the constructor
		super(Blacksmith, self).__init__() #super() function calls the init from Base class which is Character(object)
		#super(present class name, self).__init__()
bs = Blacksmith()
print(bs.health) #print 100

class Character(object): #Character is the Base class
	def __init__(self,name):  #init calls the constructor, name is a funciton to be inherited
		self.health = 100
		self.name = name
	def printName(self):
		print(self.name)
class Archer(Character):  #Archer is the Inheriting class.  It's inheriting the Base class Character
	def __init__(self, name, forgeName): #init class the constructor
		super(Archer, self).__init__(name) #super() function calls the init from Base class which is Character(object) and pass name into Base class name from Archer __init__ to Character __init__
		#super(present class name, self).__init__(passingvariable)
		self.forge = Forge(forgeName) #call Forge() class?
class Forge:
	def __init__(self, forgeName):
		self.name = forgeName

ar = Archer("Bob","Rick\'s forge")
ar.printName() #return Bob
#print(ar.name) seems to work, too, to print Archer's name Bob
print(ar.forge.name) #print Rick's forge.  Access the forge from self.forge.