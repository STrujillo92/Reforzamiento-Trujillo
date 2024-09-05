lista01=['máquinas','mecánica','simulación','ética','cálculo','tecnología']
print('Los valores de mi lista inicial son estos {}.'.format(lista01))
lista01.append('mecánica')
lista01.append('seminario')
lista01.append('mecánica')
print('Los valores de la lista actualizada son estos {}.'.format(lista01))
nro_veces=lista01.count('mecánica')
print('La cantidad de veces que se repite {} en la lista es {}.'.format(lista01[1],nro_veces))
del lista01[0]
print('La lista final, tras eliminar el primer elemento es {}.'.format(lista01))