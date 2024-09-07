dicci5={}
num=int(input('Ingrese el número de contactos: '))
l1=[]
l2=[]
for i in range(num):
    l1.append(input('Ingrese el nombre del contacto: '))
    l2.append(int(input('Ingrese el teléfono del contacto: ')))
    dicci5[l1[i]]=l2[i]
print('El diccionario de contactos final es: {}.'.format(dicci5))
preg=input('Ingrese el contacto que desea buscar: ')
if preg in dicci5.keys():
    print('El teléfono de {} es {}.'.format(preg, dicci5[preg]))
else:
    print('{} no se encuentra registrado.'.format(preg))
    dicci5[preg]=int(input('Ingrese el número de {}:'.format(preg)))
print('El diccionario de contactos actual es: {}.'.format(dicci5))