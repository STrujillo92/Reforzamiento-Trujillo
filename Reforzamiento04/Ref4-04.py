class Alumno:
    nombre=''
#constructor
    def __init__(self):
        self.edad=0
        self.notaf=0
#metodos
    def pedir_datos(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.edad = int(input("Ingrese la edad del alumno: "))
        self.notaf = float(input("Ingrese la nota final del alumno: "))
    def imprimir(self):
        print('El alumno {} tiene {} años.'.format(self.nombre,self.edad))
        print('El alumno {} obtuvo {} como nota final.'.format(self.nombre,self.notaf))
    def resultado(self):
        if self.notaf>=11:
            print('El alumno {} aprobó el curso con {}.'.format(self.nombre,self.notaf))
        else:
            print('El alumno {} reprobó el curso con {}.'.format(self.nombre,self.notaf))

alum1=Alumno()
alum1.pedir_datos()
alum1.imprimir()
alum1.resultado()
alum2=Alumno()
alum2.pedir_datos()
alum2.imprimir()
alum2.resultado()
alum3=Alumno()
alum3.pedir_datos()
alum3.imprimir()
alum3.resultado()
