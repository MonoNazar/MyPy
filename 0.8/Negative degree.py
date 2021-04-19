a = float(input())
n = int(input())

def power(a, n):
    if n < 0:
        if n == -1:
            print(1)
            return 1 / a
        else:
            return 1 / a * power(a, n + 1)
    elif n == 0:
        return 1
    else:
        if n == 1:
            return a
        else:
            return a * power(a, n - 1)

print(power(a, n))


#Дано действительное положительное число a и целоe число n. Вычислите a^n. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.