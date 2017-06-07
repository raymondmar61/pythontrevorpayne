#Trevor Payne Basics 5 of 8 Exception Handling

for i in [[5,1,2,3],[4,5],[6,7]]:
	for j in i:
		if (4 < j <= 6):
			print(j) #print 5, 5, 6

for i in range(10):
	if (i % 2):
		pass
	else:
		continue
	print(i) #print 1, 3, 5, 7, 9

try:
	x = 1.0/0.0
except ZeroDivisionError:
	print("got it! I'm awesome!") #print got it! I'm awesome!
finally:
	raise TypeError("Just kidding!") #error message appears with TypeError:  Just kidding!