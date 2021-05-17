import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
#
# s = s.cumsum()
# print(s)
# s.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# wykres = grupa.plot.bar()
# wykres.set_xlabel("Kontynenty")
# wykres.set_ylabel('Populacja w mld')
# wykres.legend()
# plt.title('Populacja z podziałem na kontynenty')
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()
#
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# #standardowe rozmiary wykresy [6.4, 4,8]
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), legend=(0,0))
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

# s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
#
# s = s.cumsum()
#
# df = pd.DataFrame(s)
# df['MA'] = df.rolling(window=100).mean()
# df.plot()
# plt.show()
#=============  2czesc cwiczen ==============

# ============== praca domowa ============
# zad1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
# df = pd.read_excel('imiona.xlsx')
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# plt.show()
# zad2
# df = pd.read_excel('imiona.xlsx', header=0)
# grupa = df.groupby(['Plec']).agg({'Plec':['count']})
# wykres = grupa.plot.bar()
# plt.legend(loc='lower left')
# plt.xticks(rotation=0)
# plt.show()
# zad3
# df = pd.read_excel('imiona.xlsx', header=0)
# grupa = df.groupby(['Liczba']).agg({'Plec':['sum']})
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.show()
# zad4
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# grupa = df.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
# wykres = grupa.plot.bar()
# plt.show()