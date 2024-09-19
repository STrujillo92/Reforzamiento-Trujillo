lista=[]
def agreg_e(a):
    try:
        a=int(a)
        print('Dato válido: número entero.')
        lista.append(a)
    except ValueError:
        print('El dato ingresado no es o no puede convertirse en un número entero.')
    else:
        print('Los valores actuales en lista son: {}.'.format(lista))


def buscar(x):
    try:
        val=lista[x]
    except IndexError:
        print('Posición inválida, vuelva a intentar.')
        print('La lista actual solo tiene {} posiciones.'.format(len(lista)))
    else:
        print('El valor en la posición {} es {}.'.format(x,val))


agreg_e(2)
agreg_e(6)
agreg_e(10)
agreg_e('b')
agreg_e(4)
agreg_e(5)
agreg_e('c')
agreg_e('a')
agreg_e(23)
agreg_e(1)
buscar(3)
buscar(5)
buscar(10)

