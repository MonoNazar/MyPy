a = input()

a1 = len(a) // 2 + len(a) % 2
a2 = a[:a1]
a3 = a[a1:]
print(a3 + a2)

#Дана строка. 
#Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой части должна быть на один символ больше). 
#Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
#При решении этой задачи не стоит пользоваться инструкцией if.