def fibonacci_generator():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c


fib = fibonacci_generator()
n = 1
for i in range(35):
    print(str(n) + " число: ", next(fib))
    n += 1
