class Persona:
    nombre = ''

    # constructor
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.boni = 0
        self.meses = 0

    # metodos
    def mostrar_datos(self):
        print('La persona se llama {} y gana {} soles.'.format(self.nombre, self.sueldo))
        if self.edad >= 18:
            print('La persona {} es mayor de edad.'.format(self.nombre))
        else:
            print('La persona {} es menor de edad.'.format(self.nombre))

    def bonificacion(self):
        if self.edad >= 18:
            self.boni = self.sueldo * 0.2
            print('La persona {} recibirá un bono de {} soles.'.format(self.nombre, self.boni))
        else:
            print('La persona {} no recibirá bonificación.'.format(self.nombre))

    def preg_mes(self):
        self.meses = int(input('Ingrese el número de meses que lleva trabajando en la empresa: '))
        print('La persona {} lleva en la empresa {} meses.'.format(self.nombre, self.meses))


# Aplicando herencia, se crea subclase:
class Persona2(Persona):
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.apto = False
        self.prest = 0

    def evalua(self):
        if self.meses > 12 and self.edad > 25:
            self.apto = True
            print('La persona {} está apto para recibir un préstamo.'.format(self.nombre))
        else:
            self.apto = False
            print('La persona {} no está apto para recibir un préstamo.'.format(self.nombre))

    def monto_pres(self):
        if self.apto == True:
            self.prest = 10 * self.sueldo
            print('La persona {} puede recibir {} soles de préstamo.'.format(self.nombre, self.prest))
        else:
            print('Lamentablemente por ahora su monto para solicitar un préstamo es de {} soles.'.format(self.prest))


pers01 = Persona2('Samantha', 32, 2000)
pers01.mostrar_datos()
pers01.preg_mes()
pers01.evalua()
pers01.monto_pres()
pers02 = Persona2('Francesco', 16, 1000)
pers02.mostrar_datos()
pers02.preg_mes()
pers02.evalua()
pers02.monto_pres()
pers03 = Persona2('Henry', 50, 1500)
pers03.mostrar_datos()
pers03.preg_mes()
pers03.evalua()
pers03.monto_pres()
