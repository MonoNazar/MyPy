a = int(input())
b = int(input())

b1 = b % 2
b += (b1 - 1)
for x in range(b, a - 1, -2):
	print(x)

#Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. 
#В этой задаче можно обойтись без инструкции if.