def ope_sum(a,b):
    try:
        a = float(a)
        b = float(b)
        suma = a + b
    except ValueError:
        print('Uno o ambos datos ingresados no son numéricos.')
    else:
        print('La suma de {} y {} es {}.'.format(a,b,suma))


ope_sum(10,20)
ope_sum(80,'Hola Pythonista')