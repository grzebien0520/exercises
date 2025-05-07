#cwiczenie 8 - moduł

def liczba_doskonala():
    n = 2
    while True:
        suma = sum(i for i in range(1, n) if n % i == 0)
        if suma == n:
            yield n
        n += 1
