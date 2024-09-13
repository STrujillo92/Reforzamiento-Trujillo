class Persona:
    nombre=''
#constructor
    def __init__(self,nombre,edad,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.sueldo=sueldo
        self.boni=0
#metodos
    def mostrar_datos(self):
        print('La persona se llama {} y gana {} soles.'.format(self.nombre,self.sueldo))
        if self.edad>=18:
            print('La persona {} es mayor de edad.'.format(self.nombre))
        else:
            print('La persona {} es menor de edad.'.format(self.nombre))
    def bonificacion(self):
        if self.edad>=18:
            self.boni=self.sueldo*0.2
            print('La persona {} recibirá un bono de {} soles.'.format(self.nombre,self.boni))
        else:
            print('La persona {} no recibirá bonificación.'.format(self.nombre))

pers1=Persona('Samantha',32,2000)
pers1.mostrar_datos()
pers1.bonificacion()
pers2=Persona('Francesco',15,1000)
pers2.mostrar_datos()
pers2.bonificacion()