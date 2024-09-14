medidas = []


class Figura:
    # constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def pedir_medidas(self):
        if self.nombre == 'rectangulo':
            base = float(input('Ingrese la medida de la base(cm): '))
            medidas.append(base)
            altura = float(input('Ingrese la medida de la altura(cm): '))
            medidas.append(altura)
        elif self.nombre == 'circulo':
            radio = float(input('Ingrese la medida del radio(cm): '))
            medidas.append(radio)
        else:
            print('Nombre de figura es inválido. Solo admite rectangulo o circulo.')


class Rectangulo(Figura):
    def __init__(self, nombre):
        self.nombre = nombre

    # metodos
    def area(self):
        self.area = medidas[0] * medidas[1]
        print('El área del rectángulo es de {} cm2.'.format(self.area))

    def perimetro(self):
        self.peri = 2 * (medidas[0] + medidas[1])
        medidas.clear()
        print('El perímetro del rectángulo es de {} cm.'.format(self.peri))


class Circulo(Figura):
    def __init__(self, nombre):
        self.nombre = nombre

    # metodos
    def area(self):
        self.area = 3.14159 * pow(medidas[0], 2)
        print('El área del círculo es de {} cm2.'.format(self.area))

    def perimetro(self):
        self.peri = 2 * 3.14159 * medidas[0]
        medidas.clear()
        print('El perímetro del círculo es de {} cm.'.format(self.peri))


fig1 = Figura('rectangulo')
fig1.pedir_medidas()
rect1 = Rectangulo('rectangulo')
rect1.area()
rect1.perimetro()
fig2 = Figura('circulo')
fig2.pedir_medidas()
circ1 = Circulo('circulo')
circ1.area()
circ1.perimetro()
fig3 = Figura('rectangulo')
fig3.pedir_medidas()
rect2 = Rectangulo('rectangulo')
rect2.area()
rect2.perimetro()
fig4 = Figura('circulo')
fig4.pedir_medidas()
circ2 = Circulo('circulo')
circ2.area()
circ2.perimetro()