lista09=[]
tamano=int(input('Ingrese el número de empresas de TI: '))
for i in range(tamano):
    lista09.append(input('Ingrese una empresa de TI: '))
print('Las empresas en la lista son: {}.'.format(lista09))
lista10=lista09.copy()
tamano2=int(input('Indique cuántas empresas agregará: '))
for i in range(tamano2):
    lista10.append(input('Ingrese nombre de empresa a agregar: '))
print('Las empresas en la nueva lista son: {}.'.format(lista10))
listafinal=[]
for i in lista10:
    if lista10.count(i)==1:
        listafinal.append(i)
print('Los elementos no repetidos de la lista son: {}.'.format(listafinal))
print('La lista inicial es la siguiente {}.'.format(lista09))