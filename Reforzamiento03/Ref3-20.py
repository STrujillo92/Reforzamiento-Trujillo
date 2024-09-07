dicci4={}
num=int(input('Ingrese el número de alumnos: '))
l1=[]
l2=[]
for i in range(num):
    l1.append(input('Ingrese el nombre del alumno: '))
    l2.append(int(input('Ingrese la nota del alumno: ')))
    dicci4[l1[i]]=l2[i]
for i in range(num):
    print('La nota {} es {}.'.format(l1[i],l2[i]))
print('El diccionario de notas final es: {}.'.format(dicci4))