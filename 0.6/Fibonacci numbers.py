i = int(input())

a = 0
b = 1 

for x in range(i):
	c = a + b
	a = b
	b = c
	print(c)	