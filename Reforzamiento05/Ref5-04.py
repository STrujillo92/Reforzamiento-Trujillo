from datetime import datetime, date

fecha=datetime.now()

def saludo():
    nom=input('Ingrese el nombre: ')
    anio=fecha.year
    mes=fecha.month
    dia=fecha.day
    try:
        a=int(nom)
    except ValueError:
        print('Hello {}, hoy estamos {} de {} del {}.'.format(nom,dia,mes,anio))
    else:
        print('Nombre ingresado incorrecto.')

saludo()
