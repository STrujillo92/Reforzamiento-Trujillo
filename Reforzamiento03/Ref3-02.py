lista01=['máquinas','mecánica','simulación','ética','cálculo','tecnología']
print('Los valores de mi lista inicial son estos {}.'.format(lista01))
lista01.append('álgebra')
lista01.append('comercio')
lista01.append('lenguaje')
lista01.append('seminario')
print('La lista con los nuevos elementos son {}.'.format(lista01))
lista01.remove('mecánica')
lista01.remove('ética')
print('La lista de elementos final es {}.'.format(lista01))
print('La cantidad de elementos en la lista final es {}.'.format(len(lista01)))
