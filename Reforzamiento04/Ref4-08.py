class Persona:
    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.impu = 0

    # metodos
    def calc_imp(self):
        print('{} gana {} soles.'.format(self.nombre, self.sueldo))
        if self.sueldo > 4000:
            self.impu = 0.1 * self.sueldo
            print('{} debe pagar {} soles de impuestos.'.format(self.nombre, self.impu))
        else:
            print('{} no debe pagar impuestos.'.format(self.nombre))


emp1 = Empleado('Samantha', 32, 3500)
emp1.calc_imp()
emp2 = Empleado('Henry', 50, 6000)
emp2.calc_imp()
