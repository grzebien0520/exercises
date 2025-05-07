import random
from generator import generator
from fibbonaci import fibonacci
from kwadraty import kwadraty
from liczby_doskonale import liczba_doskonala

def main():
    #cwiczenie 1
    print("-------------------")
    print("1. Napisz funkcję generatora, która generuje liczby parzyste z podanego zakresu.")
    generator()
    print("-------------------")

    #cwiczenie 2
    print("2. Stwórz listę składaną zawierającą potęgi liczb od 1 do 10.")
    powers_of_numbers = [x ** 2 for x in range(1, 11)]
    print(powers_of_numbers)
    print("-------------------")

    #cwiczenie 3
    print("3. Napisz program, który wykorzystuje generator do stworzenia listy zawierającej liczby parzyste i nieparzyste z podanej listy liczb.")
    numbers = [random.randint(1, 100) for _ in range(10)]
    i = 10

    odd_numbers = []
    even_numbers = []
    while i > 0:
        for x in numbers:
            if x % 2 == 0:
                even_numbers.append(x)
            elif x % 2 == 1:
                odd_numbers.append(x)
        i = - 1

    print(f"List of numbers: {numbers}")
    print(f"List of odd numbes: {odd_numbers}")
    print(f"List of even numbers: {even_numbers}")
    print("-------------------")

    #cwiczenie 4
    print("4. Zaimplementuj generator, który zwraca kolejne elementy ciągu Fibonacciego.")
    print(fibonacci)
    print("-------------------")

    #cwiczenie 6 (wiem, że nie w kolejności ale tak mi było wygoniej robić, 5 zajmę się później.)
    print("6. Stwórz generator, który zwraca liczby pierwsze.")
    numbers1 = [random.randint(1, 100) for _ in range(10)]
    prime_numbers = []
    for i in numbers1:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            prime_numbers.append(i)
        elif i == 2 or i == 3 or i == 5 or i == 7:
            prime_numbers.append(i)
        else:
            continue

    print(f"List of generated numbers: {numbers1}")
    print(f"List of prime numbers: {prime_numbers}")
    print("-------------------")

    #cwiczenie 7
    print("7. Napisz funkcję, która przyjmuje listę liczb i zwraca sumę kwadratów tylko tych liczb, które są większe od 10.")
    numbers2 = sorted([random.randint(1, 20) for _ in range(10)])
    print(f"List of generated numbers: {numbers2}")
    print(f"List of squares numbers grater than 10: {kwadraty(numbers2)}")
    print("-------------------")

    #cwiczenie 8
    print("8. Zaimplementuj generator, który generuje kolejne liczby doskonałe.")
    doskonala = liczba_doskonala()    #przy większym zasięgu program działa bardzo wolno bądź się zacina,
    for i in range(3):                #to była najprostrza i wsumie jedyna metoda jaka wymyśliłem na rozwiązanie tego zadania,
        print(next(doskonala))        #jeśli zna Pani korzystniejszą metode na rozwiązanie tego zadania to chętnie ją poznam, pozdrawiam.
    print("-------------------")

    #cwiczenie 9
    print("9. Stwórz listę składaną, która filtruje liczby parzyste z podanej listy liczb.")
    z = sorted([random.randint(1, 100) for _ in range(10)])
    even_list = [z for z in z if z % 2 == 0]
    print(f"List of numbers: {z}")
    print(f"List of even numbers: {even_list}")
    print("-------------------")

    #cwiczenie 10
    print("10. Napisz program, który korzysta z generatora i listy składanej do stworzenia listy zawierającej trzykrotne potęgi liczb z podanej listy")
    another_list = [random.randint(2, 10) for _ in range(5)] #Chodzi o potege 3 stopnia?
    cubed = [i ** 3 for i in another_list]
    print(f"List of numbers: {another_list}")
    print(f"List of cubed numbers: {cubed}")
    print("-------------------")

    #cwiczenie 5
    print("5. Napisz program, który wykorzystuje listę składaną do stworzenia listy zawierającej litery tekstu wraz z ich długościami.")
    sentence = ("Cwiczenia z Pythona są super!")
    result = [(word, len(word)) for word in sentence.split()]
    print(f"Tuple of words: {result}") #Mam nadzieje, że o to chodziło w tym zadaniu.
    print("-------------------")
if __name__ == '__main__':
    main()