#Trevor Payne 12 OOP 3 of 3 Abstract Classes, Multiple Inheritance

#abstract base class can't be instantiated.  Only inherited from.  Build subclasses only.  May also be called "Virtual".
#abstract classes prevente base class from being instantiated.  Force functions with exact name to be defined
from abc import ABCMeta, abstractmethod
class BaseClass(object):
	__metaclass__ = ABCMeta
	@abstractmethod #decorator.  A way of altering functions or classes without having to inherit or subclasses
	def printham(self):
		pass
class InheritanceClass(BaseClass):
	def printham(self):
		print("ham")
#x = BaseClass() #error message because Can't instantiate abstract class BaseClass with abstract methods printham which appears in python2.7. @abstractmethod and __metaclass__ is an abstract base class.  Nothing happens in python 3.5.
x = InheritanceClass()
x.printham()

#multiple inheritance
#A subclass inherits from multiple Base classes
from abc import ABCMeta, abstractmethod
class Enemy(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def attackPlayer(self,player):
		pass
class EnvironmentAsset(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def __init__(self):
		self.mobile = False
class Trap(Enemy, EnvironmentAsset):
	def __init__(self):
		super(Trap,self).__init__()
	def attackPlayer(self,player):
		return player.health - 10
x = Trap()		