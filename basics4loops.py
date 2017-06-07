#Trevor Payne Basics 4 of 8 Loops

#loops repeat actions over and over with less code; e.g. wash a dish repeat scrub
#functions, btw, combine many actions in a single process covered later; e.g. clean a kitchen many areas to clean

#while loop condition is true do this over and over
x = 0
while (x < 10):
	print(x)
	x += 1
print("\n")
x = 0
while (x < 10):
	x += 1
	print(x)
#break is used to stop a loop
#while (true): if (something): break
x,y = 0,0
while True:
	print(x, y)
	x+=1
	y+=2
	if ((x + y) > 10):
		print("Done")
		break

#for loop for each item in list or range, loop
x = [1, 2, 7]
for eachitem in x:
	print(eachitem) #print 1\n 2\n 7\n
for eachnumber in range(10,30,2):
	print(eachnumber) #print 10, 12, 14, 16, . . . 26, 28
#continue is used to start loop over on next value if in for loop
print("\n")
for eachnumbernot3 in range(0,30):
	if not (eachnumbernot3 % 3 != 0):
		continue
	print(eachnumbernot3) #print 1, 2, 4, 5, 7, 8, 10, 11, . . . 26, 28, 29.  No numbers divisible by 3.
print("\n")
for eachnumbernot3b in range(0,30): #same results appear.
	if (eachnumbernot3b % 3 == 0):
		continue
	print(eachnumbernot3b)