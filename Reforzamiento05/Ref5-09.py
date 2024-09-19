from datetime import datetime, date

tiempo=datetime.now()

def funcionADecoradora(funcionB):

    def funcionC():
        print('Buenos días.')
        funcionB()
        print('Hasta luego, que tenga un buen día.')
    return funcionC()


@funcionADecoradora
def saludo():
    nom=input('Ingrese su nombre: ')
    hora=tiempo.hour
    minutos=tiempo.minute
    print('Buenos días {}, son las {} horas con {} minutos.'.format(nom,hora,minutos))