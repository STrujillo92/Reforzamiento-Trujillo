"""
11. Identificar qué tipo de dato se obtiene al elevar un número a la exponente de 5 y
luego dividirlo por 10. Mostrar el resultado de su módulo con 3 en pantalla
"""

num=10
ope1=pow(num,5)
ope2=ope1/10
print("El tipo de dato del número tras las operaciones es: {}.".format(type(ope2)))
ope3=ope2%3
print("El residuo de dividir el último número entre 3 es de {}.".format(ope3))