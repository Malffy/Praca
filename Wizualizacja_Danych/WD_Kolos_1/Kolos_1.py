import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as op
import scipy as sp
#panadas 1.4.0
#matplotlib 3.5.1
#numpy 1.22.2

# Kolos 2

# Zadanie 1
# x = np.linspace(1, 20, 20)
# plt.plot(x, x**2+4*x/np.sin(x), 'r', label='f(x) = x**2+4*x/np.sin(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.xlim(1, 20)
# plt.title('Wykres funkcji f(x) = f(x) = x**2+4*x/np.sin(x) dla x[1,20]')
# plt.legend()
# plt.show()


# Zadanie 2
# plt.subplot(2, 2, 2)
# x = np.linspace(-2, 2, 40)
# y = np.tan(x)*np.sin(x)
# plt.plot(x, y, 'g--', label="tan(x)*sin(x)")
# plt.xlabel("x")
# plt.ylabel("wynik funkcji")
# plt.title("Pierwszy wykres")
# plt.xlim(-2, 2)
# plt.legend(loc="lower center")
#
#
# plt.subplot(2, 2, 3)
# a = np.linspace(-3, 3, 40)
# b = np.sin(x) + np.tan(x)
# plt.plot(a, b, "b", label="sin(x) + tan(x)")
# plt.xlabel("x")
# plt.ylabel("wynik funkcji")
# plt.title("Drugi wykres")
# plt.legend(loc="upper right")
# plt.xlim(-3, 3)
# plt.savefig("imie_nazwisko_zad2.png")
# plt.show()

# Zadanie 3
# df = pd.read_csv("iris.data", sep=",", decimal=".")
# a = df[df["class"]=="Iris-versicolor"]
# sns.set()
# sns.scatterplot(x=a["petal length"], y=a["petal width"], color="red")
# plt.title("Wykres punktowy")
# plt.show()

# Zadanie 4
# df = pd.read_csv("automobile.csv", sep=";", decimal=".")
# sns.set()
# plot = sns.barplot(data=df, x='Car model', y='Price', estimator=np.sum)
# plt.title("Wykres kolumnowy")
# plt.show()

# Egzamin

# żeby nan się pozbyć do df.dropna()
# zawsze o to prosi
# tak
# df.T - zamienia wiersze z kolumnami
# dropna()
# najpierw musisz mieć nan
# w datafrejmie
# potem piszesz nowy_df = df.dropna()
#tak samo nowy_df = df.T



# #Nazywamy kolumny
# df.columns =['rynek', 'Metraz', 'Rok', 'ilosc']
# print(df)
# #wybieramy jaki typ wartości nas interesuje
# grupa=df[df['rynek']=='rynek wtórny']
# #Czy sumujemy czy Średnia
# grupa=grupa.groupby('Metraz').agg({'ilosc':'sum'})
#
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
# plt.legend(title='metraż')
# plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2 roku')
# plt.show()
# #wybieramy jaki typ wartości nas interesuje
# grupa=df.where(df['rynek']=='rynek pierwotny')
# #Czy sumujemy czy Średnia
# grupa=grupa.groupby('Metraz').agg({'ilosc':'sum'})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
# plt.legend(title='metraż')
# plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
# plt.show()

# Egzamin 2 z teams

# Zadanie 1
# plt.subplot(1, 2, 1)
# b = np.array(['A', 'B', 'C', 'D', 'E'])
# c = np.array([36, 49, 15, 42, 40])
# plt.barh(b, c, color=['blue', 'pink', 'orange', 'grey', 'purple'])
# plt.title('Wykres lewy')
# plt.xticks(np.arange(0, 41, 10))
# plt.subplot(1,2,2)
# d = np.array([-30, -35, -40, -38, -30])
# plt.barh(b, d, color=['pink', 'cyan', 'cyan', 'brown', 'green'])
# plt.title('Wykres prawy')
# plt.xticks(np.arange(-30, 0, 10))
# plt.show()

# Zadanie 2
# xlsx = pd.read_excel('ceny2.xlsx')
# df = pd.DataFrame(xlsx)
# print(df)
# a = df.groupby('Rodzaje towarów').agg({'Wartość': ['mean']})
# print(a)
# b= df[df['Rodzaje towarów']=='ryż - za 1kg']
# c= df[df['Rodzaje towarów']=='mąka pszenna - za 1kg']
# ax = plt.subplot(1,1,1)
# plt.plot(b['Rok'], b['Wartość'],label='Ryż')
# plt.plot(c['Rok'], c['Wartość'],label='Mąka')
# plt.legend(loc='lower right')
# plt.title('Ceny')
# plt.text(1 , 0,'11:20',va='bottom', ha='right', transform=ax.transAxes)
# plt.show()

# Zadanie 3
# csv = pd.read_csv('nieruchomosci2.csv', sep = ';')
# df = pd.DataFrame(csv)
# df=df.T
# print(df)
# plt.pie(df[2])
# plt.show()



# Egzamin 3

# Zadanie 1
# a = np.array(['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'])
# b = np.array([4, 22, 7, 13, 38, 33])
# c = np.array([-17, -34, -9, -25, -20, -3])
# plt.barh(a, b, color='purple', label='A')
# plt.barh(a, c, color='red', label='B')
# plt.title('Wykres zmian A i B')
# plt.legend(loc='upper left')
# plt.show()

# Zadanie 2
# xlsx = pd.read_excel('produkcja3.xlsx')
# df = pd.DataFrame(xlsx)
# print(df)
# ax = plt.subplot(1,1,1)
# sizes = np.array([5,10,15,20,25,30,35,40,45])
# x = df['Rok']
# y = df['Wartość']
# plt.scatter(x,y, color='red', s=sizes, label='siemanko')
# plt.text(1 , 0,'11:20',va='bottom', ha='right', transform=ax.transAxes)
# plt.legend(loc='upper left')
# plt.title('Najleszpy wykres Świata')
# plt.show()

# Zadanie 3
# csv = pd.read_csv('sport3.csv', sep='!')
# df = pd.DataFrame(csv)
# print(df)
# a = df[df['Płeć']=='Mężczyźni']
# b = df[df['Płeć']=='Kobiety']
# plt.subplot(1,2,1)
# plt.pie(a['Popularność'],labels=['Piłka nożna','Koszykówka','Siatkówka','Inne'],shadow=True)
# plt.title('Mężczyźni')
# plt.subplot(1,2,2)
# plt.pie(b['Popularność'],labels=['Piłka nożna','Koszykówka','Siatkówka','Inne'],shadow=True)
# plt.title('Kobiety')
# plt.show()

# Egzamin próbny z yt 1

# Zadanie 1

# x = np.arange(-5, 10, step=0.01)
# y = (4 - x + x ** 3) / (6 + x - 4 * x ** 2 + x ** 3)
# plt.plot(x, y, color="lightblue", label="Funkcja")
# plt.ylim(-30, 30)
# # asympotota pozioma
# av = np.ones(len(x))
# plt.plot(x, av, color="orange", linestyle="--", label="y=1")
# # asymptota pionowa
# x1 = [-1, -1]
# y1 = [-30, 30]
# plt.plot(x1, y1, color="red", linestyle="--", label="x=-1")
# x2 = [2, 2]
# y2 = [-30, 30]
# plt.plot(x2, y2, color="green", linestyle="--", label="x=2")
# x3 = [3, 3]
# y3 = [-30, 30]
# plt.plot(x3, y3, color="violet", linestyle="--", label="x=3")
# plt.title("Wykres funkcji")
# plt.legend()
# plt.savefig("zad1.pdf", format="pdf")
# plt.show()

# Zadanie 2
# dane = pd.read_excel("sport.xlsx", header=None)
# x = dane.iloc[:, 1]
# etykiety = dane.iloc[:, 0]
# plt.pie(x, labels=etykiety, autopct="%1.0f%%", explode=(0.1, 0, 0, 0, 0, 0))
# plt.title("Popularność sportu w grupie nastolatków")
# plt.annotate("12345", [-1, 1])
# plt.savefig("zad2.jpg")
# plt.show()

# Zadanie 3
# dane = pd.read_csv("wyksz.csv")
# wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
# sred = dane[dane["Wykształcenie"] == "średnie"]
# podst = dane[dane["Wykształcenie"] == "podstawowe"]
# x = np.arange(0, len(wyzsze))
# plt.bar(x - 0.25, wyzsze["Liczebność"], label="Wyższe", width=0.25, color="blue")
# plt.bar(x, sred["Liczebność"], label="Średnie", width=0.25, color="green")
# plt.bar(x + .25, podst["Liczebność"], label="podstawowe", width=0.25, color="brown")
# plt.legend(loc=7)
# plt.ylabel("Liczebność")
# plt.xlabel("Przedział wiekowy")
# plt.title("Wykształcenie a wiek")
# plt.xticks(x, wyzsze["Wiek"])
# plt.show()
