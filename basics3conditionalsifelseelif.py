#Trevor Payne Basics 3 of 8 Conditionals, If, Else, Elif

mail = 5
if mail:
	print("mail time!") #print mail time!
mail = 0
if mail:
	print("mail time!")	
else:
	print("no mail :(") #print no mail :( because 0 is false

if (4 < 6):
	print("ham sandwich") #print ham sandwich
if (7 <= 6):
	print("whaaa")
else:
	print("7 is greater than 6")  #print 7 is greater than 6

if (7) and (6): #there are two values in the paranthesis which are true
	print("yup") #print yup
if (0) and (4):
	print("wahaaa") #print nothing because 0 is False
if not (0):
	print("yep") #print yep because 0 is false, not false is true.

j = "jam"
if (j == "jams"):
	print("jams time")
elif (j == "jam"):
	print("jam time") #print jam time
else:
	print("no jam time")