class Persona:
#constructor
    def __init__(self):
        self.nombre = ''
        self.apellido = ''
#metodos
    def pedir_nombre(self):
        self.nombre = input('Ingrese su nombre: ')
        self.apellido = input('Ingrese su apellido: ')
    def pedir_edad(self):
        self.edad = int(input('Ingrese su edad: '))
    def mostrar(self):
        dicci1={'nombre':self.nombre,'apellido':self.apellido,'edad':self.edad}
        print('El diccionario de datos de la persona es: {}.'.format(dicci1))

pers1=Persona()
pers1.pedir_nombre()
pers1.pedir_edad()
pers1.mostrar()
