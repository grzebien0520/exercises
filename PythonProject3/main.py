from book import Book
from punkt import punkt3D
from palindrome import palindrome
import sys
#cw 4, 5
def srednia(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
#cw 6,7
def fibonacci(n):
    if n < 0:
        raise ValueError("Indeks musi być liczbą nieujemną.")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
#cw 10
examples = ["kajak", "Anna", "Jakub", "Python"]

def main():
    #1, 2
    def sum_even_numbers(numbers):
     return sum(num for num in numbers if num % 2 == 0)
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Suma liczb parzystych:", sum_even_numbers(list))
    #3
    # Tworzenie obiektów książek
    book1 = Book("tralala", "Jakub", 2025)
    book2 = Book("Rok 1984", "George Orwell", 1949)
    book3 = Book("Harry Potter", "JK Rowling", 2040)

    # Wyświetlanie informacji o książkach
    books = [book1, book2, book3]
    for book in books:
        print(book.get_title())
        print(book.get_author())
        print(book.get_year())
    # 4,5
    example_numbers = [14, 22, 36, 48, 52]
    print("Średnia:", srednia(example_numbers))
    # 6,7
    index = 10
    print(f"{index}-ty element ciągu Fibonacciego: {fibonacci(index)}")
    # 8,9
    p1 = punkt3D(1, 2, 3)
    print(p1.distance_to_origin())
    #10
    for text in examples:
        print(f'"{text}" jest palindromem: {palindrome(text)}')
    return 0
if __name__ == "__main__":
    main()


