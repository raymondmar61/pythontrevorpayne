#Trevor Payne Basics 2 of 8 Strings, Lists, Tuples and Dictionaries

a = str(int(2.23) + float(14)) + " tomatoes"
print(a) #print 16.0 tomatoes

print("ham Ham".upper()) #print HAM HAM
print("SUPER Baba".lower()) #print super baba

b = "I am ham"
print(b.split()) #print ['I','am','ham']
print(b.split("m")) #print ['I a', ' ha', '']
print(b.join(a)) #print 1I am ham6I am ham.I am ham0I am ham I am hamtI am hamoI am hammI am hamaI am hamtI am hamoI am hameI am hams  Joins variables a = 16.0 tomatoes and b = "I am ham"

print("int: %d, float %.5f" % (14.4, 55.2)) #print int: 14, float 55.20000

l = [1,6,7,26,8,3,4,5]
print(l[:]) #print [1, 6, 7, 26, 8, 3, 4, 5]
print(l[:2]) #print [1, 6]
print(l[2:]) #print [7, 26, 8, 3, 4, 5]
print(l[::2]) #print [1, 7, 8, 4]
print(l[1::2]) #print [6, 26, 3, 5]

list2 = [1, 2, 3]
listx = [5, 6, list2]
print(listx) #print [5, 6, [1, 2, 3]]

y = [1, 2, 3, 1, 5, 2, 1, 3]
z = list(set(y))
print(z) #print [1, 2, 3, 5]

myDict = {14: "Ham", 20: "Sandwich"}
print(myDict.keys()) #print dict_keys([20, 14])
print(myDict.values()) #print dict_values(['Sandwich', 'Ham'])
print(len(myDict)) #print 2
