# Zad 1
# a = ["Piłka nożna", "Koszykówka", "Siatkówka"]
# print(a)
# a.reverse()
# print(a)
# a.append("Narciarstwo")
# print(a)

# Zad 2, 3
# a = {'np': 'na przykład', 'pt': 'pod tytułem'}
# b = {'FPS': "Counter Strike", 'MOBA': "League of M0nkeys"}
# print(len(b))

# Zad 4
# a = input("Podaj zdanie :")
# print(a.count("a"))

# Zadanie 5
# import sys
# sys.stdout.write("Podaj a (calkowita): ")
# a = int(sys.stdin.readline())
# sys.stdout.write("Podaj b (calkowita): ")
# b = int(sys.stdin.readline())
# sys.stdout.write("Podaj c (calkowita): ")
# c = int(sys.stdin.readline())
# wynik=(a**b) + c
# sys.stdout.write(str(wynik))

# Zadanie 6
# a = input("Podaj liczbe a:")
# b = input("Podaj liczbe b:")
# c = input("Podaj liczbe c:")
# a = int(a)
# b = int(b)
# c = int(c)
# if a >= b & b >= c:
#     print("Liczba",a ,"jest najwieksza")
# elif b >= a & a >= c:
#     print("Liczba",b ,"jest najwieksza")
# else:
#     print("Liczba",c ,"jest najwieksza")

# Zadanie 7
# a = [2, 3, 4, 2.5, 5.5]
# for x in a:
#     print(x**2)

# Zdanie 8
# x = 1
# a = []
# while x<=10:
#     z=int(input())
#     if z % 2 == 0:
#         a.append(z)
#     x+=1
#


# Zadanie 9
# import math
#
# a = input("Podaj liczbe: ")
# a = int(a)
# try:
#     print(math.sqrt(a))
# except ValueError:
#     print("Liczba ujemna z pierwiastka? Wracaj do licbazy.")
