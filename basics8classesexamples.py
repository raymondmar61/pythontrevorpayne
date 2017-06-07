#Trevor Payne Basics 8 of 8 Classes

class Ham:
	def __init__(self):
		self.name = "ham"
		self.healthBonus = 10
class Hero:
	def __init__(self):
		self.health = 100
	def eat (self, food):
		self.health += food.healthBonus
bob = Hero()
ham = Ham()
# bob.eat(turkey) error message turkey is not defined
# print(bob.health)
bob.eat(ham)
print(bob.health) #print 110

class AddFive:
	def add(self, var):
		return var + 5
class Num:
	def __init__(self, value):
		self.val = value
		self.otherVal = None
n = Num(15)
a5 = AddFive()
n.otherVal = a5.add(n.val)
print(n.val, n.otherVal) #print 15, 20
