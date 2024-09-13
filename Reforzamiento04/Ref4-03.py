class Circulo:
#constructor
    def __init__(self):
        self.radio = 0
#metodos
    def pedir_radio(self):
        self.radio = float(input("Ingrese el radio: "))
    def area(self):
        self.area = 3.1416*pow(self.radio,2)
        print('El área del círulo es de {} cm2.'.format(self.area))

    def perimetro(self):
        self.perimetro = 2*3.14156*self.radio
        print('El perímetro del círulo es de {} cm.'.format(self.perimetro))

circ01=Circulo()
circ01.pedir_radio()
circ01.perimetro()
circ02=Circulo()
circ02.pedir_radio()
circ02.perimetro()