import random
from colorsys import yiq_to_rgb
from math import sqrt

l=[]
l2=[]
def agregar():
    x=int(input('Ingrese un número: '))
    y=int(input('Ingrese un número: '))
    z=int(input('Ingrese un número: '))
    l.append(x)
    l.append(y)
    l.append(z)
    print(l)


def suma2():
    suma=l[0]+l[1]
    print(suma)


def aleatorios():                   #buscado de j2logo para generar números aleatorios
    for i in range(30):
        x=random.randint(1,100)
        l2.append(x)
    return l2


def ordenar(a):
    a.sort()
    print(a)


def el_max(a):
    num=a[-1]
    print(num)


def selec_num():
    num=None
    x=input('Ingrese un número: ')
    try:
        num=int(x)
    except ValueError:
        print('Valor ingresado no es numérico, reintentar.')
    return num


def raiz(a):
    try:
        res=sqrt(a)
    except TypeError:
        print('El valor ingresado no es numérico.')
    else:
        print('La raíz cuadrada de {} es {}'.format(a,res))


def potencias(a):
    try:
        x=pow(a,2)
        y=pow(a,3)
    except TypeError:
        print('El valor ingresado no es numérico.')
    else:
        dicci={'cuadrado':x,'cubo':y}
        print(dicci)


