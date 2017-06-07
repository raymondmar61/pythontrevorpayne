#Trevor Payne Basics 1 of 8 Integers, Floats and Maths

#variables are containers for any kind of data.  name = value

import math
var = 5
print(var) #print 5
anythingiwant = 70
print(anythingiwant) #print 70
anythingiwant = 80
print(anythingiwant) #print 80
print(5+6) #print 11
print(5**2) #print 25
print(10 % 5) #print 0
print(3/2) #print 1.5
print(3.0/2.0) #print 1.5
print(int(3.0/2.0)) #print 1
print(500.0/250) #print 2.0
print("Python recognize float numbers as float numbers.  Any one number with a decimal Python converts the number to float.  Also, float() works.")
print(float(5**2)) #print 25.0
print("More math functions:  abs() absolute value, floor() round down, ceil() round up, pow() power or expontent.  floor() and ceil() need math module")
print(abs(-6)) #print 6
print(math.floor(45.4)) #print 45.  Needs math module math dot (.)
print(float(math.floor(45.4))) #prints 45.0.  Needs math module math dot (.)
print(math.ceil(45.4)) #print 46.  Needs math module math dot (.)
print(float(math.ceil(45.4))) #prints 46.0.  Needs math module math dot (.)
print(pow(5,2)) #print 25