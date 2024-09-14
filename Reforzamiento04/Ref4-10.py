l2 = []


class Soldado:
    posx = 0
    posy = 0

    # constructor
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.nom = input('Ingrese el nombre del soldado: ')

    # metodos
    def mover_x(self):
        pasos = int(input('Cuántos pasos dará {} en el eje X: '.format(self.nom)))
        self.posx = self.posx + pasos
        print('La posición actual de {} es X:{} Y:{}.'.format(self.nom, self.posx, self.posy))

    def mover_y(self):
        pasos = int(input('Cuántos pasos dará {} en el eje Y: '.format(self.nom)))
        self.posy = self.posy + pasos
        if self.posy < 0:
            self.posy = 0
        print('La posición actual de {} es X:{} Y:{}.'.format(self.nom, self.posx, self.posy))

    def ubicacion(self):
        l1 = [self.posx, self.posy]
        l2.append(l1)
        print('Las posiciones que ha ocupado {} son: {}.'.format(self.nom, l2))


sol1 = Soldado(10, 5)
sol1.mover_x()
sol1.ubicacion()
sol1.mover_y()
sol1.ubicacion()
sol1.mover_y()
sol1.ubicacion()
sol1.mover_y()
sol1.ubicacion()
sol1.mover_x()
sol1.ubicacion()
sol1.mover_x()
sol1.ubicacion()