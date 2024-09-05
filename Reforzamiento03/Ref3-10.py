lista07=['Arequipa','Ica','Loreto','Cusco','Puno']
dep01=input('Ingrese el primer departamento elegido: ')
dep02=input('Ingrese el segundo departamento elegido: ')
print('La lista inicial es la siguiente: {}.'.format(lista07))
lista07.append(dep01)
print('La lista actualizada es la siguiente: {}.'.format(lista07))
lista07[-1]=dep02
print('La lista final es la siguiente: {}.'.format(lista07))
