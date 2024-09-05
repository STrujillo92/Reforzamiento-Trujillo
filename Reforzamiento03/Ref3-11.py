lista08=['clientes','productos','facturas','categorias','ventas']
print('La lista de bases  de datos inicial es: {}.'.format(lista08))
bd1=input('Ingrese la base de datos a eliminar: ')
n_veces=lista08.count(bd1)
if n_veces>0:
    lista08.remove(bd1)
else:
    print('La base de datos elegida no estaba en la lista. Será agregada.')
    lista08.append(bd1)
print('La lista de bases de datos actual es: {}.'.format(lista08))