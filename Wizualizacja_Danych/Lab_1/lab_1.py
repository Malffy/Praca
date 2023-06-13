import sys
import math

# print(sys.version)
#
# a='inżynieria\nsystemów\ninformatycznych\n'
# print(a)
# print(type(a))
#
# b=5
# print(b)
# print(type(b))
#
# c=5.5
# print(c)
# print(type(c))
#
# d=2+3j
# print(d)
# print(type(d))
#
# #nowa_zmienna(CTRL+/)
#
# # del a
# # print(a)
#
# e='isi'
# f=' grupa 4'
# print(e+f)
#
# g=7
# h=2
# print(g//h) #dzielenie całkowite
# print(g**h) #Podnoszenie do potęgi !Uwaga na kolejność działań! (lepsza jest biblioteka math)
# print(math.pow(g,h)) #Lepsza opcja

a=5
b=3
c=a+b
print('wynik działania %(z1)d+%(z2)d= %(z3)d' %{'z1':a,'z2':b,'z3':c})
print('wynik działania {0:d} + {1:d}= {2:d}'.format(a,b,c))