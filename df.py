import pandas as pd
import matplotlib.pyplot as plt

countries_df = [
    ("Polska", "Europa", 38),
    ("Niemcy", "Europa", 83),
    ("Francja", "Europa", 67),
    ("Włochy", "Europa", 60),
    ("Hiszpania", "Europa", 47),
    ("Rosja", "Europa/Azja", 144),
    ("Chiny", "Azja", 1412),
    ("Indie", "Azja", 1393),
    ("Japonia", "Azja", 126),
    ("Korea Południowa", "Azja", 52),
    ("USA", "Ameryka Północna", 331),
    ("Kanada", "Ameryka Północna", 38),
    ("Meksyk", "Ameryka Północna", 128),
    ("Brazylia", "Ameryka Południowa", 213),
    ("Argentyna", "Ameryka Południowa", 45),
    ("Chile", "Ameryka Południowa", 19),
    ("Australia", "Australia/Oceania", 26),
    ("Nowa Zelandia", "Australia/Oceania", 5),
    ("Egipt", "Afryka", 104),
    ("Nigeria", "Afryka", 206),
    ("RPA", "Afryka", 60),
    ("Etiopia", "Afryka", 118),
    ("Turcja", "Azja/Europa", 85),
    ("Arabia Saudyjska", "Azja", 35),
    ("Iran", "Azja", 85),
    ("Pakistan", "Azja", 220),
    ("Indonezja", "Azja", 273),
    ("Tajlandia", "Azja", 70),
    ("Filipiny", "Azja", 113),
    ("Kolumbia", "Ameryka Południowa", 51),
    ("Wenezuela", "Ameryka Południowa", 28),
    ("Peru", "Ameryka Południowa", 33),
    ("Sudan", "Afryka", 45),
    ("Kenia", "Afryka", 54),
    ("Maroko", "Afryka", 37),
]

kolumna = ['Panstwo', 'Kontynent', 'Populacja (mln)']
swiat = pd.DataFrame(countries_df, columns = kolumna)

sorted = swiat.sort_values('Populacja (mln)', ascending=False)
sorted.reset_index(drop=True, inplace=True)

plt.figure(figsize = (16, 8))
plt.bar(sorted['Panstwo'], sorted['Populacja (mln)'])

plt.xticks(rotation = 90)
plt.ylabel('Populacja (mln)')
plt.title('Wykres ludnosci panstw')

print(sorted)
plt.show()
