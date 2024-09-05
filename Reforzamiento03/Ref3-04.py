lista01=['máquinas','mecánica','simulación','ética','cálculo','tecnología']
lista02=[]
lista02.append(input("Ingrese su nombre: "))
lista02.append(input("Ingrese su apellido: "))
lista02.append(input("Ingrese su carrera: "))
lista02.append(int(input("Ingrese su edad: ")))
lista02.append(int(input("Ingrese en que mes estamos: ")))
lista02.append(int(input("Ingrese el número del día de hoy: ")))
lista02.append(float(input("Ingrese su talla: ")))
lista02.append(float(input('Ingrese su peso: ')))
lista02.append(float(input('Ingrese el número de horas promedio que trabaja a la semana: ')))
print('La lista con los datos del personal es la siguiente {}'.format(lista02))
sum_listas=lista01+lista02
print('El resultado de sumar ambas listas es {}'.format(sum_listas))