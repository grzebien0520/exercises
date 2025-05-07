#cwiczenie 4 - modul

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
fibonacci = []
for i in range(15):
    fibonacci.append(next(fib))


