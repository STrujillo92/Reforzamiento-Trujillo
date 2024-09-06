dicci1={'nombre':'samantha','edad':32,'salario':1500.0,'carrera':'ingeniería'}
dicci1['dni']=70477228
#print('El valor de salario es: {}.'.format(dicci1['salario']))
del dicci1['edad']
print('El diccionario actualizado es: {}'.format(dicci1))
l1=list(dicci1.values())
for i in l1:
    print('El tipo de dato es: {}'.format(type(i)))
