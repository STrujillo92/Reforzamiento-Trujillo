dicci2={'dep1':'Arequipa','dep2':'Ica','dep3':'Lima','dep4':'Cusco','dep5':'Puno','dep6':'Tacna'}
print('Los departamentos en el diccionario inicial son {}.'.format(dicci2.values()))
del dicci2['dep4']
l1=list(dicci2.keys())
if l1.count('dep4')==0:
    print('Departamento borrado')
else:
    print('Departamento permanece en lista.')
print('Los departamentos en el diccionario final son: {}.'.format(dicci2.values()))

