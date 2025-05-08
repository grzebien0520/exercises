#Cwiczenia zaliczeniowe 1 semestr Python Jakub Grzebielucha, Jakub59599
from collections import deque
import math
import random
#Lista 1, Lista 2, Lista 3
#cwiczenie 1
print("-----------")
print("Program wypisujący liczbe:")
x = 8
print(x)

#cwiczenie 2
print("-----------")
print("Program proszący o podanie imienia:")
print(input("Write your name: "))

#cwiczenie 3
print("-----------")
print("Program liczący czy podane wartości kwalifikują się pod wiek emerytalny:")
print("M = man, K = woman")
try:
    M = int(input("Write your age: "))
    K = M
    a = input("Write M if you are a man or K if you are a woman: ").upper()
    if a == "M":
            if M > 65:
                print("You qualify for retirement!")
            elif M >= 0 and M <= 65:
                print("You are not eligible for retirement!")
            else:
                raise ValueError

    if a == "K":
            if K > 60:
                print("You qualify for retirement!")
            elif K >= 0 and K <= 60:
                 print("You are not eligible for retirement!")
            else:
                raise ValueError

except ValueError:
    print("Error: Write your real age!")

#ćwiczenie 4
print("-----------")
print("Program liczący czy z podanych boków powstanie trójkąt:")
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("This is a triangle.")
    else:
        print("This is not a triangle.")

triangle(1, 1, 5) #To nie jest trójkąt
triangle(3, 3, 5) #To jest trójkąt

#lista 4, lista 5
#ćwiczenie 1
print("-----------")
print("Program wypisujący informacje o studentach:")
inf_student = {"name": ["Mariusz", "Grzegorz", "Krzesisław"], "surname": ["Golonka", "Dygas", "Sandomierski"], "age": [21, 19, 26]}
print(f"Student named: {inf_student["name"][1]}, and surname: {inf_student["surname"][1]}, has {inf_student["age"][1]} years old.")

#ćwiczenie 2
print("-----------")
print("Program ukazujący niemutowalność krotki:")
tuple = ("Anna", "Jan", "Maria")
try:
    tuple.append("Jakub")
    print(tuple)
except AttributeError:
    print("Error: tuple is immutable.")

#cwiczenie 3
print("-----------")
print("Program wypisujący posortowaną liste:")
sorted_list = [5, 2, 8, 1, 3]
sorted_list.sort()
sorted_list.pop(1)
print(sorted_list)

#cwiczenie 4
print("-----------")
print("Program wypisujący pracowników zarabiających więcej niż 5000 (PLN):")
workers = [["Anna", "Wesołowska", "sprzątaczka", 3500], ["Katarzyna", "Tomczyk", "Kierowniczka", 7500], ["Andrzej", "Gołota", "Przełożony", 5300]]
for worker in workers:
    name, surname, position, salary = worker
    if salary > 5000:
        print(f"Worker named: {name} and surname {surname}, on position: {position}, earns: {salary} (PLN).")


#cwiczenie 5
print("-----------")
print("Program pokazujący wartość imię z 1 słownika:")
info_slownik = {"name": "Jakub", "surname": "Biały", "age": 19}, {"name": "Kacper", "surname": "Piącha", "age": 23}
print(info_slownik[0]["name"])

#cwiczenie 6
print("-----------")
print("Program pokazujący 3 element z 1 krotki:")
letters_tuple = ((1, 2, 3), (4, 5, 6))
number_to_show = letters_tuple[0][2]
print(number_to_show)

#lista 6
#cwiczenie 1
print("-----------")
print("Program zwracajacy liste pełnych imion i nazwisk:")
names = ["Anna", "Jan", "Maria"]
surnames = ["Kowalska", "Nowak", "Wiśniewska"]

def full_names(names, surnames):
     return [f"{name} {surname}" for name, surname in zip(names, surnames)]
name = full_names(names, surnames)
print(name)

#cwiczenie 2
print("-----------")
print("Program liczący wartość oceny razem z jej indexem:")
grades = [3, 5, 2, 1, 4]
for index, grade in enumerate(grades):
    print(f"Grade: {grade}, Index: {index}")

#cwiczenie 3
print("-----------")
print("Program liczący długość słownika:")
dictionary_lenght = {"math", "IT", "physics", "chemistry", "geography"}
lenght = len(dictionary_lenght)
print(lenght)

#cwiczenie 4
print("-----------")
print("Program tworzący symulacje kolejki:")
queue = deque()

def add_queue(item):
    queue.append(item)
    print(f"Added {item} to the queue.")

def remove_queue():
    if queue:
        item = queue.popleft()
        print(f"Removed {item} from queue.")

def show_queue():
    if queue:
        print("Queue contents:", list(queue))
    else:
        print("Queue is empty.")

add_queue("car")
show_queue()
remove_queue()
show_queue()

#lista 7
#cwiczenie 1
print("-----------")
print("Funkcja sprawdza czy podane argumenty są anagramami:")

def anagram(word1, word2):
    for i in word1:
        if i in word2:
            print("The word is an anagram.")
            return True
        else:
            print("The word is not an anagram.")
            return False

anagram("robak", "barok") #Powinien wyjsc anagram
anagram("pies", "mysz") #Nie powinien wyjsc anagram

#cwiczenie 2
print("-----------")
print("Program liczący pole koła (w cm):")

def circle_area(r):
   try:
    if r > 0:
        return print("Circle area is:", int(math.pi * (r ** 2)), "cm.")
    else:
        return print("The radius of a circle cannot be a negative number.")
   except TypeError as err:
       print("Error: Print a letter.", err)


circle_area(8) #Circle area is: 201 cm.
circle_area(-4) #The radius of a circle cannot be a negative number.
circle_area("kolo") #Error: Print a letter. '>' not supported between instances of 'str' and 'int'

#cwiczenie 3
print("-----------")
print("Program generujący liczbe z przedziału od 1 do 100 i sprawdzający czy jest ona liczbą pierwszą:")

def prime_number():
    x = random.randint(1, 100)
    print(x)
    if x == 2 or x == 3 or x == 5 or x == 7:
        print(f"Number {x} is a prime number.")
    elif x >= 2 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        print(f"Number {x} is a prime number.")
    else:
        print(f"Number {x} is not a prime number.")
    return x

prime_number()

#Lista 8
#cwiczenie 1
print("-----------")
print("Program wypisujący tylko wyrazy zawierające w sobie literke (a):")

list_words = ["car", "dog", "bicycle", "emerald", "blinker"]
def word_with_a(letters):
    list_with_a = []
    for i in letters:
        if "a" in i:
            list_with_a.append(i)
    return list_with_a

print(word_with_a(list_words))
#cwiczenie 2
print("-----------")
print("Program wypisujący kwadraty liczb w liscie:")
list_letters = [4.2, 12, 3.4, 7.2, 10, 1, 8.9]
def square(list):
    list_full_letter = []
    for i in list:
        full_letter = int(i)
        list_full_letter.append(full_letter ** 2)
    return list_full_letter

print(square(list_letters))
#cwiczenie 3
print("-----------")
print("Funkcja wypisująca najdroższy produkt ze słownika:")
products = {"chair": 100, "table": 150, "water": 3}
def most_expensive(products):
    return max(products, key=products.get)
print(most_expensive(products))

#lista 9
#cwiczenie 1
print("-----------")
print("Klasa wypisująca informacje o książce:")

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def book_info(self):
        print(f"Name: {self.name}\nAuthor: {self.author}\nYear: {self.year}")

    def year_of_book(self):
        return self.year < 2000

Book1 = Book("Zycie Jakuba", "Jakub", 1999)
Book2 = Book("Tralala", "Jakub59599", 2020)
Book1.book_info()
print("Was published before 2000:", Book1.year_of_book())
Book2.book_info()
print("Was published before 2000:", Book2.year_of_book())

#cwiczenie 2
print("-----------")
print("Program umożliwiający edytowanie zawartosci koszyka:")

class Product:
    def __init__(self, name, value, amount):
        self.name = name
        self.value = value
        self.amount = amount

    def add_to_cart(self, amount):
        self.amount += amount

    def reduce_quantity(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("The quantity cannot be reduced below zero.")

    def cart_value(self):
        return self.value * self.amount


# Przykład użycia
product1 = Product("Laptop", 3500, 2)
product1.add_to_cart(1)
print("Cart value:", product1.cart_value())
product1.reduce_quantity(2)
print("New quantity in cart:", product1.amount)

#cwiczenie 3
print("-----------")
print("Program umożliwiający obliczenie pola i obwodu trójkąta:")

class FiguraGeometryczna:
    def area(self):
        pass

    def circle(self):
        pass


class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def circle(self):
        return self.a + self.b + self.c


tr1 = Trojkat(3, 4, 5)
print("The area of the triangle is:", tr1.area())
print("The perimeter of the triangle is:", tr1.circle())


#cwiczenie 4
print("-----------")
print("Program dziedziczący po klasie pojazd i dodający atrybuty:")

class Pojazd:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

class Samochod(Pojazd):
    def info(self, przebieg):
        print(f"Pojazd marki: {self.marka}, model: {self.model}, rok produkcji: {self.rok_produkcji} rok, o przebiegu: {przebieg} km.")
        return
class Motocykle(Pojazd):
    def moto_info(self, silnik):
        print(f"Pojazd marki: {self.marka}, model: {self.model}, rok produkcji: {self.rok_produkcji} rok, o pojemnosci silnika: {silnik} litrow.")
        return


auto = Samochod("Renault", "clio", 2008)
auto_info = auto.info(140000)
print(auto_info)
motor = Motocykle("BMW", 4, 2018)
motor_info = motor.moto_info(2)
print(motor_info)

#lista 10
#cwiczenie 1
print("-----------")
print("Program liczacy pole kola i kwadratu:")

class Kwadrat:
    def __init__(self, bok):
        self.bok = bok
    def oblicz_pole(self):
        return self.bok ** 2

class Kolo:
    def __init__(self, promien):
        self.promien = promien
    def oblicz_pole(self):
        return math.pi * self.promien ** 2

figury = [Kwadrat(4), Kolo(2)]
for figura in figury:
    print(f"Pole {figura.__class__.__name__}, wynosi: {figura.oblicz_pole()}")

#cwiczenie 2
print("-----------")
print("Program zabezpieczajacy atrybuty imie i nazwisko:")

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.wiek = wiek

    def get_imie(self):
        return self.__imie

    def set_imie(self, imie):
        self.__imie = imie

    def get_nazwisko(self):
        return self.__nazwisko

    def set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def __str__(self):
        return f"{self.__imie} {self.__nazwisko}, wiek: {self.wiek}."

osoba = Osoba("Jakub", "Grzebielucha", 20)
print(osoba)

# Zmiana imienia za pomocą settera
osoba.set_imie("Grzegorz")
print(osoba.get_imie())

#cwiczenie 3
print("-----------")
print("Program z metoda abstrakcyjna daj glos() dla zwierzat:")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("How How")

class Cat(Animal):
    def getVoice(self):
        print("meow meow")

dog = Dog("Burek",10)
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Jakub",8)
print(cat.name)
cat.getVoice()

#cwiczenie 4
print("-----------")
print("Dekorator mnozacy wynik funkcji razy 2:")

def multiply_by_two(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_by_two
def get_number():
    return 8

print(get_number())

#KONIEEEEEEEEEEEEEEEEC :DDDDDDDDDDD