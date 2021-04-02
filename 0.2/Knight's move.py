a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if a1 == b1 and a2 == b2:
	print("no")
elif a1 == b1 - 1 or a1 == b1 + 1:
	if a2 == b2 - 2 or a2 == b2 + 2:
		print("yes")
	else:
		print("no")	
elif a1 == b1 - 2 or a1 == b1 + 2:
	if a2 == b2 - 1 or a2 == b2 + 1:
		print("yes")
	else:
		print("no")	
else:
	print("no")


#Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. 
#Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.