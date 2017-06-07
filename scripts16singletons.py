#Trevor Payne 16 Singletons

#singletons are a design pattern.  Only one object instance may exist at any given time.  Instructor teachs longer way and then shorter way using a decorator.

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