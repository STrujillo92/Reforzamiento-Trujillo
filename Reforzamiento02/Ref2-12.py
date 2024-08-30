"""
12. Crear una lista con diferentes tipos de datos (enteros, flotantes, string y
booleans), crear una lista con  número pares y sumarlo a la anterior lista para luego
mostrarlos en pantalla (observar y comentar que sucede al sumar listas)
"""

lista1=[8,3.15,"abc",False,12,"Python",True]
lista2=[2,4,6,8,10]
lista3=lista1+lista2
print("La lista resultante es la siguiente: {}.".format(lista3))
"""
Las listas admiten operaciones como la suma y también que haya elementos repetidos. Además,
las posiciones que guarda cada elemento si tienen importancia, porque estas se mantienen tras la operación.
Los nuevos elementos se agregan al final de la lista.
"""