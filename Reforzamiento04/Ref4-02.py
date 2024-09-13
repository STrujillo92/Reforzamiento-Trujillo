class Circulo:
#constructor
    def __init__(self,radio):
        self.radio = radio
#metodos
    def area(self):
        self.area = 3.1416*pow(self.radio,2)
        print('El área del círulo es de {} cm2.'.format(self.area))

circ01=Circulo(4.5)
circ01.area()