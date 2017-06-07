#Trevor Payne Basics 6 of 8 Functions

def returnTwo():
	return 20, 30
print(returnTwo()) #returns tuple (20, 30)
x = returnTwo()
print(x) #returns tuple (20, 30)
y, z = returnTwo()
print(y,z) #returns 20 30

#works Python2.7.  Returns 3628800
# def mul(x, y):
# 	return x * y
# FACTORIAL
# print(reduce(mul, range(1,11)))

#works Python2.7.  Returns [1, 8, 27, 64, 125, 216, 343, 512, 729, 10000]
#Python3.5 returns map object <map object at 0x7fc6718016d8>
def cubeFunc(x):
	#Returns the cube of value passed in
	return x * x * x
print(map(cubeFunc,range(1,11)))

def myAdd(var1, var2 = 10):
	return var1 + var2
print(myAdd(7)) #returns 17
print(myAdd(8, 5)) #returns 13