n = int(input())
a, b, c = 0, 1, 1


def fib(n):
    global a, b, c
    c = a + b
    b = c
    a = b
    if n == 1:
        return c
    else:
        return a + fib(n - 1)

print(fib(n))
