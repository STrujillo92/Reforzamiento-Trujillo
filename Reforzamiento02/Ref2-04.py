"""
4. Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe
estar en una variable. Mostrar el volumen por pantalla.
"""

valor1=4/3
valor2=3.141593
radio=8.2
volumen=valor1*valor2*pow(radio,3)
volumen_red=round(volumen,2)
print("El volumen de una esfera con radio de {} cm es de {} cm3.".format(radio,volumen_red))