#Trevor Payne Basics 4 of 8 Loops

#fibonacci sequence
fiboseq = []
a = 0
b = 1
while (b < 1000):
	fiboseq.append(a)
	#a,b = b, a + b #not a=b, b = a + b
	temp_a = a
	print("temp_a=a temp_a:" ,temp_a)
	a = b
	print("a=b a:" ,a)
	b = temp_a + b
	print("b=temp_a+b b:" ,b)
	print("\n")
print(fiboseq)

factorial = 0
for i in range(30):
	print(factorial)
	factorial+=i
print(factorial)

primes = []
for i in range(2, 100):
	for x in range(2, i):
		if (i % x == 0):
			break
	else:
		primes.append(i)
print(primes)
