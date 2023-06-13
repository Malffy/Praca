import random
# Zadanie 1
# a = [(random.randint(0,30))*2 for i in range(10)]
# a = str(a)
# plik = open("liczby.txt","w+")
# plik.writelines(a)
# plik.close()

# Zadanie 2
# plik = open("liczby.txt","r")
# print(plik.readlines())
# plik.close()

# Zadanie 3
# a = """asdasdasd
# asdasdasdasdasd
# asdasdasdasdas
# dsadasdasdasd"""
# with open('zad3.txt', 'w') as plik:
#     for linia in a:
#         plik.write(linia)
# with open('zad3.txt', 'r') as plik:
#     for a in plik:
#         print(a)

# Zadanie 4
# class NaZakupy():
#     def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("{}, {} {} w cenie {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))
#
#     def ile_produktu(self):
#         print("{} {}".format(self.ilosc, self.jednostka_miary))
#
#     def ile_kosztuje(self):
#         return float(self.ilosc) * float(self.cena_jed)
#
# maselko = NaZakupy("masło","2","sztuki",2.5)
# maselko.wyswietl_produkt()
# maselko.ile_produktu()
# print(maselko.ile_kosztuje())

# Zadanie 5
class arytm:

    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.an = [self.a1 + (self.r * i) for i in range(self.n)]

    def wyswietl_dane(self):
        print(self.an)

    def pobierz_elementy(self, *an):
        self.an = [x for x in an]

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.an = [self.a1 + (self.r * i) for i in range(self.n)]

    def policz_sume(self):
        return sum(self.an)

    def policz_elementy(self):
        return ((self.an[-1] - self.a1) / self.r) + 1

c = arytm(1, 1, 10)
c.wyswietl_dane()

c.pobierz_elementy(1, 3, 5)
c.wyswietl_dane()

c.pobierz_parametry(2, 5, 5)
c.wyswietl_dane()

print(c.policz_sume())
print(c.policz_elementy())

# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y = self.y + ile_krokow * self.krok
#
#     def idz_w_dol(self, ile_krokow):
#         self.y = self.y - ile_krokow * self.krok
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x = self.x - ile_krokow * self.krok
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x = self.x + ile_krokow * self.krok
#
#     def gdzie(self):
#         print("x: " + str(self.x))
#         print("y: " + str(self.y))
#
#
# elo = Robaczek(1, 1, 3)
# elo.idz_w_lewo(2)
# elo.idz_w_prawo(3)
# elo.idz_w_dol(5)
# elo.idz_w_gore(10)
# elo.gdzie()

