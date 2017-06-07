#Trevor Payne 11 OOP 2 of 3 Overriding Variables And Functions And Organizing Files

#A variable in the base class can be overwritten in the inheritance class.
#Why override?  Ensures a variable is attached to a class; if an Inheritance class doesn't have a variable, the Base class variable is the default.  Prevents program from crashing.

class BaseClass(object):
	def __init__(self):
		self.x = 10
class InheritanceClass(BaseClass):
	def __init__(self):
		super(InheritanceClass, self).__init__()
		self.x = 20
instance = InheritanceClass()
#The BaseClass created self.x = 10.  In InheritanceClass, we redefine self.x = 20.  We overrode the initial value.
print(instance.x) #print 20

class BaseClass2(object):
	def test(self):
		print("ham")
class InheritanceClass2(BaseClass):
	def test(self):
		print("hammer time")
instance2 = InheritanceClass2()
#BaseClass2 function was overriden with same name and same parameters in InheritanceClass2 function test(self)
instance2.test() #return hammer time

#separating files  Separate each BaseClass.  BaseClass gets its own file.
class BaseClass3(object):
	def test(self):
		print("ham")
class InheritanceClass3(BaseClass):
	def test(self):
		print("hammer time")
print(BaseClass.__subclasses__()) #print [<class '__main__.InheritanceClass'>, <class '__main__.InheritanceClass2'>, <class '__main__.InheritanceClass3'>].  Function shows subclasses from main class.