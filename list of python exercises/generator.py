#cwiczenie 1 - modul

import random

def generator():
    i = random.randint(1, 100)
    if i % 2 == 0:
        print(i)
    else:
        print(f"{i} is odd. So it shouldn't be printed, but it is there for checking the numbers.")
