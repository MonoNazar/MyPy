a = float(input())
n = int(input())

def power(a, n):
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)

print(power(a, n))


#Дано действительное положительное число a и целоe число n. Вычислите a^n. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.