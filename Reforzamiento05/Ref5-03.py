dicci={}
def agre_con():
    a=input("Ingrese el nombre del usuario: ")
    b=input("Ingrese el apellido del usuario: ")
    try:
        a.isdigit()==False #idea de esta función con el ejercicio con isalnum (busqueda en google)
        b.isdigit()==False
    except ValueError:
        print('Datos de nombre y/o apellido inválidos.)')
    else:
        dicci['nombre'] = a
        dicci['apellido'] = b
    c = input("Ingrese el dni del usuario: ")
    try:
        x=int(c)
        dicci['dni'] = c
    except ValueError:
        print('Dato del dni inválido.')
    else:
        print('Los datos del usuario ingresado son: {}.'.format(dicci))


def buscar(a):
    try:
        x=dicci[a]
    except KeyError:
        print('La clave ingresada es incorrecta.')
    else:
        print('El valor buscado de la clave {} es {}.'.format(a,x))


agre_con()
buscar('nombre')
buscar('apellido')
buscar('profesion')