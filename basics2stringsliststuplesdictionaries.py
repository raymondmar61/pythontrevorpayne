#Trevor Payne Basics 2 of 8 Strings, Lists, Tuples and Dictionaries

x = "ham"
print(x) #print ham
y = x + "book"
print(y) #print hambook
y = x + " spacebook"
print(y) #print ham spacebook
x = "hamsandwich"
z = 10
y = x + (str(z)) 
print(y) #print hamsandwich10
y = "something %d something %d" % (z, z)
print(y) #print something 10 something 10
print("Integer number %d Float number %f Float number 3 decimal places %.3f" % (z, z, z)) #print Integer number 10 Float number 10.000000 Float number 3 decimal places 10.000
z = 1.6546546548
print("Integer number %d Float number %f Float number 3 decimal places %.3f" % (z, z, z)) #print Integer number 1 Float number 1.654655 Float number 3 decimal places 1.655

#\n is new line character
print("test\ntest2\n\ntest3")
print("test\ntest2\n\n test3")
#\t is tab character
print("yes\tyes2\t\tyes3")
print("yes\tyes2\t\t yes3")
#"in" keyword used to check if a value is within another value.  Returns True or False.
print("ham" in "hamsandwich") #print True
print("ham" in x) #print True

#lists.  Data structure used for storing all data types int, float, string, etc.
list1 = []
print(list1) #print []
list1 = ["ham",4,2.2]
print(list1) #print ['ham', 4, 2.2]
list1.append("Add to list1 using append() function")
print(list1) #print ['ham', 4, 2.2, 'Add to list1 using append() function']
list1.insert(1,"Add at position 1 or index 1 in list")
print(list1) #print ['ham', 'Add at position 1 or index 1 in list', 4, 2.2, 'Add to list1 using append() function']
list1.pop(1) #pop() deletes an entry in a list.  Note position in square brackets.  Position is index number.
print(list1) #print ['ham', 4, 2.2, 'Add to list1 using append() function']
del(list1[2]) #del() also deletes an entry in a list.  Note position in square brackets.  Position is index number.
print(list1) #['ham', 4, 'Add to list1 using append() function']
#list can also convert an item to a list.  list(item) converts item to a list.  Breaks item into individual characters
print(list("abcdefghijklmnopqrstuvwxyz")) # prints ['a', 'b', 'c', 'd', 'e' . . . 'x', 'y', 'z']

#len() returns the total number of items within a string or list.  len is short for length.
print("The length \"words\" is",len("words")) #print The length "words" is 5
list2 = ["ham",4,2.2,5]
print(list2) # print ['ham', 4, 2.2, 5]
print(len(list2)) #print 4

#"in" keyword can also be used to find something in a list []
list2 = ["ham",4,2.2,5]
print("ham" in list2) #True
print(3 in list2) #False

#tuples are list lists.  Tuples are unadjustable.  It's like a grocery list with no return policy.  Tuplies take less memory than lists.
tuple1 = ("ham", 4, 5)
print(tuple1) #print ("ham", 4, 5)

#dictionaries aka hashtable, map.  Used for binding keys to values pair together.  Just like a phone book.  Name to phone number pair together.
#A colon separates each key for its value
sam = {"age": 700}
print(sam) #print {"age": 700}
sam["weapon"] = "chainsaw"
sam["health"] = 10
print(sam) #print {'age': 700, 'health': 10, 'weapon': 'chainsaw'}
print(sam["age"]) #print 700
sam["age"] = 701
print(sam["age"]) #print 701
del sam["health"]
print(sam) #{'age': 701, 'weapon': 'chainsaw'}