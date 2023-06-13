# a = [x**2 for x in range(10)]
# print(a)
# b = [3**y for y in range(6)]
# print(b)
# c = [x for x in a if x % 2 ==1]
# print(c)

# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# a = [x for x in liczby if x % 2 == 0]
#
# b = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]

# skroty = {"PZU": "Państwowy zakład ubezpieczeń",
#           "ZUS": "Zakład ubezpieczeń społecznych",
#           "PKO": "Państwowa kasa oszczędności"}
#
# odwrocone = {value: key for key, value in skroty.items()}
# print(odwrocone)

# import math
# def row_kwadratowe(a, b, c):
#     delta = (b**2)-(4*(a*c))
#     if delta>0:
#         x1 = (-b - math.sqrt(delta)) / (2 * a)
#         x2 = (-b + math.sqrt(delta)) / (2 * a)
#         return x1, x2
#     elif delta==0:
#         x = (-b) / (2*a)
#         return x
#     else:
#         return print("Funkcja nie ma miejsc zerowych")

# def ciag(* a):
#     if len(a) == 0:
#         return 0
#     else:
#         suma = 0
#         for x in a:
#             suma += x
#         return suma
#
# print(ciag(5,2,3))

# def to_lubie(** rzeczy):
#     for x in rzeczy:
#         print("To jest")
#         print(x)
#         print("co lubie")
#         print(rzeczy[x])
#
#
# to_lubie(slodycze="czekolada", rozrywka=['gry', 'filmy'])

# Zadanie 1
# a = [1-x for x in range(1,11,1)]
# print(a)
# b = [4**y for y in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zadabie 2
# import random
# lista1 = [random.randint(1, 10) for x in range(10)]
# print(lista1)
# lista2= [x for x in lista1 if x % 2 == 0]
# print(lista2)

# Zadanie 3
# produkty = {"banan": "szt.", "cukier": "kg"}
# produkty2 = {value: key for key, value in produkty.items()}
# print(produkty2)

# Zadanie 4
# def czy_prostokatny(a,b,c):
#     if (a**2 + b**2) == c**2:
#         return print("Trojkat jest protkokatny")
#     else:
#         return print("Trojkat nie jest prostokatny")
#
# czy_prostokatny(3,4,6)

# Zadanie 5
# def pole_trapezu(a=1,b=2,h=3):
#     pole = ((a + b) * h)/2
#     return pole
#
# print(pole_trapezu())

# Zadanie 6

# def iloczyn_ciagu(a=1, b=4, ile=10):
#     licznik = 0
#     for licznik in range(ile):
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn_ciagu())

# Zadanie 7

# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         for a in range(1, len(liczby), 1):
#             iloczyn_liczb *= b
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))

# Zadanie 8
# def lista_zakupow(** rzeczy):
#     koszt = 0
#     for x in rzeczy:
#         koszt += rzeczy[x]
#     return len(rzeczy), koszt
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))

# Zadanie 9
from ciagawka import *

print(arytm.n(1, 1, 50))
print(geome.sn(1, 2, 5))

# def ciag(a = 1, b = 4, ile = 10):
#     licznik = 0
#     for licznik in range(ile):
#         a *=b
#         licznik += 1
#     return a
#
# print(ciag())
